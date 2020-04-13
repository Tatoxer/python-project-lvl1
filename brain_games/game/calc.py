#!/usr/bin/env python3
from brain_games import game_logic


def calc():
    game_logic.welcome_to_game()
    name = game_logic.welcome_user()
    game_logic.rules_of_game("What is the result of the expression?")
    right_answers = 0

    while right_answers < 3:
        if right_answers == -1:
            break

        answer = game_logic.cal_logic_result()
        ua = int(game_logic.user_answer(name))
        right_answers = game_logic.check_answer(ua, answer, right_answers)

    if right_answers != -1:
        game_logic.congrats(name)
