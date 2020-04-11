#!/usr/bin/env python3
from brain_games.game_logic import *


def calc():
    welcome_to_game()
    name = welcome_user()
    rules_of_game("What is the result of the expression?")
    right_answers = 0

    while right_answers < 3:
        answer = cal_logic_result()
        ua = int(user_answer())

        if ua == answer:
            print("Correct!")
            right_answers += 1
        else:
            print(str(ua) + " is wrong answer ;(")
            print("Correct answer was " + str(answer) + ". Let's try again")
    congrats(name)
