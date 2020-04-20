#!/usr/bin/env python3
import prompt


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?\n")
    print('Hello, ' + name.capitalize() + "!\n")
    repeat_game = True

    while repeat_game:
        print(game.DESCRIPTION)
        count_of_right_answers = 0
        score_to_win = 3

        while count_of_right_answers < score_to_win:
            question, correct_answer = game.generate_game_data()
            print("Question: " + question)
            user_answer = prompt.string("Your answer: ")

            if correct_answer != user_answer:
                print(f'{user_answer} is wrong answer ;(')
                print(f"Correct answer was {str(correct_answer)}. Let's try again")
                break
            print("Correct!")
            count_of_right_answers += 1

        if count_of_right_answers == score_to_win:
            print(f'Congratulations, {name.capitalize()}!')

        if prompt.string("\nDo you want to play again? yes/no\n") == 'yes':
            repeat_game = True
        else:
            print(f'Good luck, {name.capitalize()}!')
            repeat_game = False
