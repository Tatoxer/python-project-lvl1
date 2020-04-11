#!/usr/bin/env python3
from brain_games.game_logic import *


def even():
    welcome_to_game()
    name = welcome_user()
    rules_of_game("Answer 'yes' if number even otherwise answer 'no'")
    right_answers = 0

    while right_answers < 3:
        rand_number = generate_random_number()
        answer = is_divide_by_2(rand_number)
        print("Question: " + str(rand_number))
        ua = user_answer()

        if ua == answer:
            print("Correct!")
            right_answers += 1
        elif ua != answer and ua == "yes":
            print("'yes' is wrong answer ;(")
            print("Correct answer was 'no'. Let's try again")
        else:
            print("'no' is wrong answer ;(")
            print("Correct answer was 'yes'. Let's try again")

    congrats(name)
