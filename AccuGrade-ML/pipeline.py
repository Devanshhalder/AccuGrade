from dotenv import load_dotenv

import os
import time
import mimetypes

from google import genai
from google.genai import types

from evaluator import evaluate_answer


load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)


def generate_with_retry(
    contents,
    max_attempts=3
):
    """
    Retry temporary Gemini 503/5xx errors
    with exponential backoff.
    """

    for attempt in range(max_attempts):

        try:

            return client.models.generate_content(
                model="gemini-3.8-flash",
                contents=contents,
            )

        except Exception as error:

            error_message = str(error)

            # Retry only temporary server errors
            if (
                "503" not in error_message
                and "UNAVAILABLE" not in error_message
                and "500" not in error_message
            ):
                raise

            if attempt == max_attempts - 1:
                raise

            wait_time = 5 * (2 ** attempt)

            print(
                f"Gemini temporarily unavailable. "
                f"Retrying in {wait_time} seconds..."
            )

            time.sleep(wait_time)


def get_mime_type(file_path: str) -> str:
    """
    Determine the MIME type of the uploaded answer sheet.
    """

    mime_type, _ = mimetypes.guess_type(
        file_path
    )

    if mime_type:
        return mime_type

    extension = os.path.splitext(
        file_path
    )[1].lower()

    known_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".pdf": "application/pdf",
    }

    return known_types.get(
        extension,
        "application/octet-stream"
    )


def extract_student_answer(
    image_path: str
) -> str:
    """
    Read the student's handwritten answer
    from an image or PDF.
    """

    with open(
        image_path,
        "rb"
    ) as f:

        file_bytes = f.read()

    mime_type = get_mime_type(
        image_path
    )

    print(
        f"Processing answer sheet: "
        f"{image_path}"
    )

    print(
        f"Detected MIME type: "
        f"{mime_type}"
    )

    prompt = """
Read the student's answer from this examination answer sheet.

The answer may be handwritten.

Extract ONLY the student's answer.

Do not:

- evaluate the answer
- give marks
- correct the answer
- improve the grammar
- add information that is not written by the student
- invent missing content

Return only the student's answer as plain text.
"""

    response = generate_with_retry(
        [
            prompt,
            types.Part.from_bytes(
                data=file_bytes,
                mime_type=mime_type,
            ),
        ]
    )

    return response.text.strip()


def evaluate_image(
    image_path: str,
    question: str,
    answer_key: str,
    max_marks: float,
):
    """
    Complete AccuGrade pipeline:

    Answer Sheet
          ↓
    Handwriting / Answer Extraction
          ↓
    Student Answer
          ↓
    Answer Evaluation
          ↓
    Structured Result
    """

    student_answer = extract_student_answer(
        image_path
    )

    result = evaluate_answer(
        question=question,
        answer_key=answer_key,
        student_answer=student_answer,
        max_marks=max_marks,
    )

    return (
        student_answer,
        result
    )