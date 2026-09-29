from dotenv import load_dotenv
import os

from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

with open("answer.jpg", "rb") as f:
    image_bytes = f.read()

prompt = """
Read the handwritten student's answer in this image.

Extract ONLY the student's handwritten answer.
Do not evaluate it.
Do not give marks.
Do not rewrite or improve the answer.

Return the answer as plain text, preserving the meaning and wording as closely as possible.
"""

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/jpeg",
        ),
        prompt,
    ],
)

print("\n--- EXTRACTED ANSWER ---\n")
print(response.text)