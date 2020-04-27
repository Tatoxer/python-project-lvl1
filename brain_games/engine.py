import prompt


SCORE_TO_WIN = 3


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print('Hello, ' + name.capitalize() + "!")
    print()
    print(game.DESCRIPTION)
    count_of_right_answers = 0

    while count_of_right_answers < SCORE_TO_WIN:
        question, correct_answer = game.generate_game_data()
        print("Question: " + question)
        user_answer = prompt.string("Your answer: ")

        if correct_answer != user_answer:
            print(f"{user_answer} is wrong answer ;(")
            print(f"Correct answer was {correct_answer}. Let's try again")
            return
        print("Correct!")
        count_of_right_answers += 1

    print(f'Congratulations, {name.capitalize()}!')
