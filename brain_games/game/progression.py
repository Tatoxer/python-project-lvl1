#!/usr/bin/env python3
from brain_games import game_logic
from random import choice


def progression():
    game_logic.welcome_to_game()
    name = game_logic.welcome_user()
    game_logic.rules_of_game("What number is missing in the progression?")
    right_answers = 0

    while right_answers < 3:
        if right_answers == -1:
            break
        progr = game_logic.make_progression()
        answer = choice(progr)
        replaced_progression = game_logic.replace_progression(answer, progr)

        print("Question: " + str(replaced_progression))
        ua = game_logic.user_answer(name)
        right_answers = game_logic.check_answer(ua, answer, right_answers)

    if right_answers != -1:
        game_logic.congrats(name)
