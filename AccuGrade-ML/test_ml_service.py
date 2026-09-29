from ml_service import evaluate_answer_sheet


question = """
Briefly state the first two of the Four Noble Truths taught by Gautama Buddha.
"""

answer_key = """
1. Dukkha — the truth of suffering or dissatisfaction.
2. Samudaya — the truth concerning the cause/origin of suffering,
traditionally associated with craving.
"""

result = evaluate_answer_sheet(
    image_path="answer.jpg",
    question=question,
    answer_key=answer_key,
    max_marks=2,
)

print("\n--- ACCUGRADE ML SERVICE ---\n")

for key, value in result.items():
    print(f"{key}: {value}")