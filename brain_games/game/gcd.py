#!/usr/bin/env python3
from brain_games import game_logic


def gcd():
    game_logic.welcome_to_game()
    name = game_logic.welcome_user()
    game_logic.rules_of_game("Find the greatest common divisor of given numbers")
    right_answers = 0

    while right_answers < 3:
        a = game_logic.generate_random_number()
        b = game_logic.generate_random_number()
        print("Question: " + str(a) + " " + str(b))

        answer = game_logic.remainder_two_numb(a, b)
        ua = game_logic.user_answer(name)
        right_answers = game_logic.check_answer(ua, answer, right_answers)

    game_logic.congrats(name)
