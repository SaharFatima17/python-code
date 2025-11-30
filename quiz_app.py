quiz = {
    "What is the capital of France? ": "Paris",
    "What is 5 + 7? ": "12",
    "What is the largest planet? ": "Jupiter",
    "Who wrote Harry Potter? ": "J.K. Rowling",
    "What is the boiling point of water (°C)? ": "100"
}

def start_quiz():
    score = 0
    print("\n=== QUIZ START ===")

    for question, answer in quiz.items():
        user_ans = input(question)
        if user_ans.strip().lower() == answer.lower():
            score += 1

    print(f"\nYour Score: {score} / {len(quiz)}")

start_quiz()
