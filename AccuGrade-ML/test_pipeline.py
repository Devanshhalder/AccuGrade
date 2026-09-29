from pipeline import evaluate_image


question = """
Briefly state the first two of the Four Noble Truths taught by Gautama Buddha.
"""

answer_key = """
1. Dukkha — the truth of suffering or dissatisfaction.
2. Samudaya — the truth concerning the cause/origin of suffering,
traditionally associated with craving.
"""

student_answer, result = evaluate_image(
    image_path="answer.jpg",
    question=question,
    answer_key=answer_key,
    max_marks=2,
)

print("\n--- EXTRACTED STUDENT ANSWER ---\n")
print(student_answer)

print("\n--- ACCUGRADE FINAL EVALUATION ---\n")
print(f"Status: {result.status}")
print(f"Marks: {result.marks}/{result.max_marks}")
print(f"Confidence: {result.confidence}")
print(f"Reason: {result.reason}")

print("Missing points:")
for point in result.missing_points:
    print(f"- {point}")