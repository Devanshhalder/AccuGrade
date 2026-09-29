from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse

from ml_service import evaluate_answer_sheet

import os
import tempfile


app = FastAPI(
    title="AccuGrade ML API",
    description="AI-assisted examination evaluation service",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": "AccuGrade ML",
        "status": "running"
    }


@app.post("/evaluate")
async def evaluate(
    image: UploadFile = File(...),
    question: str = Form(...),
    answer_key: str = Form(...),
    max_marks: float = Form(...),
):
    original_filename = image.filename or "uploaded_answer.jpg"

    _, extension = os.path.splitext(original_filename)

    extension = extension.lower() or ".jpg"

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=extension
        ) as temp_file:

            temp_path = temp_file.name

            file_data = await image.read()

            temp_file.write(file_data)

        result = evaluate_answer_sheet(
            image_path=temp_path,
            question=question,
            answer_key=answer_key,
            max_marks=max_marks,
        )

        return JSONResponse(
            content=result
        )

    except Exception as error:

        error_message = str(error)

        print("\n================ ML ERROR ================")
        print(error_message)
        print("===========================================\n")

        if (
            "429" in error_message
            or "RESOURCE_EXHAUSTED" in error_message
        ):
            return JSONResponse(
                status_code=429,
                content={
                    "error": "Gemini API quota exceeded.",
                    "student_answer": "",
                    "status": "needs_review",
                    "marks": 0,
                    "max_marks": max_marks,
                    "confidence": 0,
                    "reason": "AI evaluation is temporarily unavailable because the Gemini API quota has been exceeded.",
                    "missing_points": []
                }
            )

        return JSONResponse(
            status_code=500,
            content={
                "error": error_message
            }
        )

    finally:

        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)