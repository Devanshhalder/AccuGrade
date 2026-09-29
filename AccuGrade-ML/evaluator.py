from dotenv import load_dotenv
import os
from typing import Literal

from google import genai
from pydantic import BaseModel, Field


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


class EvaluationResult(BaseModel):
    status: Literal[
        "correct",
        "partially_correct",
        "wrong",
        "needs_review"
    ]
    marks: float
    max_marks: float
    confidence: float = Field(ge=0, le=1)
    reason: str
    missing_points: list[str]


def evaluate_answer(
    question: str,
    answer_key: str,
    student_answer: str,
    max_marks: float
) -> EvaluationResult:

    prompt = f"""
You are an AI-assisted university examination evaluator.

Evaluate the student's answer against the question and official
answer key/rubric.

RULES:
- Evaluate only the academic content relevant to the question.
- Do not penalize grammar, spelling, handwriting, or writing style
  unless it changes the meaning.
- Give marks from 0 to {max_marks}.
- Identify important missing concepts.
- If the answer is ambiguous or confidence is low, use "needs_review".
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

    return EvaluationResult.model_validate_json(response.text)