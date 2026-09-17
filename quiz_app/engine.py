from quiz_app.data import QUIZ_DATA

def run_quiz(num_questions):
    score = 0
    # Limit questions to total available or requested amount
    selected_questions = list(QUIZ_DATA.items())[:num_questions]
    total = len(selected_questions)

    if total == 0:
        print("No questions available.")
        return

    for question_key, question_data in selected_questions:
        print(question_data["question"])
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == question_data["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {question_data['answer']}.\n")
            score -= 1

    # Accuracy percentage calculated after completing the quiz
    accuracy = (score / total) * 100
    print(f"Your final score: {score}/{total} ({accuracy:.2f}%)")