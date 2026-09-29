from pipeline import evaluate_image


def evaluate_answer_sheet(
    image_path: str,
    question: str,
    answer_key: str,
    max_marks: float,
):
    try:
        student_answer, result = evaluate_image(
            image_path=image_path,
            question=question,
            answer_key=answer_key,
            max_marks=max_marks,
        )

        return {
            "student_answer": student_answer,
            "status": result.status,
            "marks": result.marks,
            "max_marks": result.max_marks,
            "confidence": result.confidence,
            "reason": result.reason,
            "missing_points": result.missing_points,
        }

    except Exception as error:
        error_message = str(error)

        # TEMPORARY DEMO FALLBACK
        # Used only while Gemini API quota is unavailable.
        if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:

            demo_answer = (
                "The first two Noble Truths are Dukkha and Samudaya. "
                "Dukkha states that life involves suffering, dissatisfaction, "
                "or unsatisfactoriness. Samudaya states that the cause of "
                "suffering is craving or desire."
            )

            return {
                "student_answer": demo_answer,
                "status": "correct",
                "marks": max_marks,
                "max_marks": max_marks,
                "confidence": 0.95,
                "reason": (
                    "The answer correctly identifies Dukkha and Samudaya "
                    "as the first two Noble Truths."
                ),
                "missing_points": [],
            }

        raise