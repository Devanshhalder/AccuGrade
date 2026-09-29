from dotenv import load_dotenv
import os
from typing import Literal

from google import genai
from pydantic import BaseModel, Field


# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# Structure of the AI evaluation
class EvaluationResult(BaseModel):
    status: Literal["correct", "partially_correct", "wrong", "needs_review"]
    marks: float
    max_marks: float
    confidence: float = Field(ge=0, le=1)
    reason: str
    missing_points: list[str]


# Question
question = """
Briefly state the first two of the Four Noble Truths taught by Gautama Buddha.
"""

# Maximum marks
max_marks = 2

# Official answer key / marking rubric
answer_key = """
1. Dukkha — the truth of suffering or dissatisfaction.
2. Samudaya — the truth concerning the cause/origin of suffering,
   traditionally associated with craving.
"""

# Student answer extracted from the handwritten answer
student_answer = """
The first two of the four noble truths are:
1) The truth of suffering (dukkha): Life is inherently marked by
suffering, dissatisfaction, and pain.
2) The truth of the cause of suffering (Samudaya): Suffering is
caused by craving, desire, and attachment to things like pleasure,
possessions, and existence.
"""


prompt = f"""
You are an AI-assisted university examination evaluator.

Evaluate the student's answer against the question and official
answer key/rubric.

IMPORTANT RULES:
- Evaluate only the academic content relevant to the question.
- Do not penalize grammar, spelling, handwriting, or writing style
  unless it changes the meaning.
- Give marks from 0 to {max_marks}.
- Do not award marks for information that does not answer the question.
- Identify any important missing concepts.
- If the answer is ambiguous or the confidence is low, use
  "needs_review".
- The examiner remains the final decision-maker.

QUESTION:
{question}

OFFICIAL ANSWER KEY / RUBRIC:
{answer_key}

STUDENT ANSWER:
{student_answer}
"""


response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt,
    config={
        "response_mime_type": "application/json",
        "response_schema": EvaluationResult,
    },
)

result = EvaluationResult.model_validate_json(response.text)

print("\n--- ACCUGRADE EVALUATION ---\n")
print(f"Status: {result.status}")
print(f"Marks: {result.marks}/{result.max_marks}")
print(f"Confidence: {result.confidence}")
print(f"Reason: {result.reason}")
print("Missing points:")

for point in result.missing_points:
    print(f"- {point}")