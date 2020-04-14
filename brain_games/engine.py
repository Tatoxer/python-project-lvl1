#!/usr/bin/env python3
import prompt


def run_game(game):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    again = True

    while again:
        print(game.rules)
        right_answers = 0

        while right_answers < 3:
            question, right_answer = game.logic()
            print("Question: " + question)
            user_answer = prompt.string("Your answer: ")

            if right_answer != user_answer:
                print(f'{user_answer} is wrong answer ;(')
                print(f"Correct answer was {str(right_answer)}. Let's try again")
                break
            print("Correct!")
            right_answers += 1

        if right_answers == 3:
            print(f'Congratulations, {name.capitalize()}!')

        if prompt.string("\nDo you want to play again? yes/no\n") == 'yes':
            again = True
        else:
            print(f'Good luck, {name.capitalize()}!')
            again = False


def welcome_user():
    name = prompt.string("May I have your name?\n")
    print('Hello, ' + name.capitalize() + "!\n")
    return name
