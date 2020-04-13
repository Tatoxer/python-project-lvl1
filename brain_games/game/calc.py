#!/usr/bin/env python3
from brain_games import game_logic


def calc():
    game_logic.welcome_to_game()
    user_name = game_logic.welcome_user()
    game_logic.show_rules("What is the result of the expression?")
    right_answers = 0

    while right_answers < 3:
        if right_answers == -1:
            break

        right_answer = game_logic.do_calc_logic_result()
        user_answer = int(game_logic.user_answer(user_name))
        right_answers = game_logic.check_answer(user_answer, right_answer, right_answers)

    if right_answers != -1:
        game_logic.congrats(user_name)
