# quiz.py
def ask_question(question, options, answer):
    print(question)
    for i, option in enumerate(options, start=1 ):
        print(f"{i}. {option}")
        
    user_answer = input("Choose the correct option (1-4): ")
    return options[int(user_answer) - 1] == answer
    
def main():
    questions = [
        {
             "question": "What is the capital of France?",
             "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
             "answer": "Paris"
        },
        {
             "question": "Which planet is known as the Red Planet?",
             "options": ["Earth", "Mars", "Jupiter", "Saturn"],
             "answer": "Mars"
        },
        {
             "question": "What is the largest ocean on Earth?",
             "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
             "answer": "Pacific"
        }

    ]
    score = 0
    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            print("Correct!")
            score += 1
        else:
            print("Wrong")
    print(f"\nYour final score is: {score} out of {len(questions)}")

if __name__ == "__main__":
    main()

