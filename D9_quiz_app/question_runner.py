#question_runner.py
import score_handlling
import input_validation
import question_data
def question_run():
    score = 0
    from question_data import questions
    for question in questions:
        print(question["question"])
        for idx, option in enumerate(question["options"], start =1):
            print(f"{idx}. {option}")

        user_answer = input_validation.get_user_choice(len(question["options"]))

        if user_answer == question["answer"]:
            print("Correct!")
            score += score_handlling.correct_ans()
        else:
            print("wrong")
            score += score_handlling.wrong_ans()
    print(f"\nQuiz Completed! Your final score: {score} out of {len(questions)}")