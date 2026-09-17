from quiz_app import run_quiz

user_input = input("How many questions do you want to attend? ")
if user_input.isdigit():
    run_quiz(int(user_input))