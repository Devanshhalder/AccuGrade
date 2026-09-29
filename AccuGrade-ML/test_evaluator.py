from evaluator import evaluate_answer


question = """
Briefly state the first two of the Four Noble Truths taught by Gautama Buddha.
"""

answer_key = """
1. Dukkha — the truth of suffering or dissatisfaction.
2. Samudaya — the truth concerning the cause/origin of suffering,
traditionally associated with craving.
"""

student_answer = """
The first two of the four noble truths are:
1) The truth of suffering (dukkha): Life is inherently marked by
suffering, dissatisfaction, and pain.
2) The truth of the cause of suffering (Samudaya): Suffering is
caused by craving, desire, and attachment to things like pleasure,
possessions, and existence.
"""

result = evaluate_answer(
    question=question,
    answer_key=answer_key,
    student_answer=student_answer,
    max_marks=2
)

print("\n--- ACCUGRADE REUSABLE EVALUATOR ---\n")
print(f"Status: {result.status}")
print(f"Marks: {result.marks}/{result.max_marks}")
print(f"Confidence: {result.confidence}")
print(f"Reason: {result.reason}")
print("Missing points:")

for point in result.missing_points:
    print(f"- {point}")