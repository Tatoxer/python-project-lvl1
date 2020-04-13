#!/usr/bin/env python3
from brain_games.game_logic import welcome_to_game, welcome_user, rules_of_game
from brain_games.game_logic import cal_logic_result, user_answer, congrats, check_answer


def calc():
    welcome_to_game()
    name = welcome_user()
    rules_of_game("What is the result of the expression?")
    right_answers = 0

    while right_answers < 3:
        answer = cal_logic_result()
        ua = int(user_answer(name))
        right_answers = check_answer(ua, answer, right_answers)

    congrats(name)
