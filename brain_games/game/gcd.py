#!/usr/bin/env python3
from brain_games import game_logic


def gcd():
    game_logic.welcome_to_game()
    user_name = game_logic.welcome_user()
    game_logic.show_rules("Find the greatest common divisor of given numbers")
    right_answers = 0

    while right_answers < 3:
        if right_answers == -1:
            break

        number_1 = game_logic.generate_random_number()
        number_2 = game_logic.generate_random_number()
        print("Question: " + str(number_1) + " " + str(number_2))

        right_answer = game_logic.remainder_two_numb(number_1, number_2)
        user_answer = game_logic.user_answer(user_name)
        right_answers = game_logic.check_answer(user_answer, right_answer, right_answers)

    if right_answers != -1:
        game_logic.congrats(user_name)
