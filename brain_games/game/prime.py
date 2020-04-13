#!/usr/bin/env python3
from brain_games import game_logic


def prime():
    game_logic.welcome_to_game()
    name = game_logic.welcome_user()
    game_logic.rules_of_game('Answer "yes" if given number is prime. Otherwise answer "no"')
    right_answers = 0

    while right_answers < 3:
        if right_answers == -1:
            break
        number = game_logic.generate_random_number()
        answer = game_logic.is_prime(number)

        print("Question: " + str(number))
        ua = game_logic.user_answer_yes_no()
        right_answers = game_logic.check_answer_yes_no(ua, answer, right_answers)

    if right_answers != -1:
        game_logic.congrats(name)
