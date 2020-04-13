#!/usr/bin/env python3
from brain_games import game_logic


def even():
    game_logic.welcome_to_game()
    user_name = game_logic.welcome_user()
    game_logic.show_rules("Answer 'yes' if number even otherwise answer 'no'")
    right_answers = 0

    while right_answers < 3:
        if right_answers == -1:
            break

        rand_number = game_logic.generate_random_number()
        right_answer = game_logic.is_divide_by_2(rand_number)
        print("Question: " + str(rand_number))
        user_answer = game_logic.user_answer_yes_no()

        right_answers = game_logic.check_answer_yes_no(user_answer, right_answer, right_answers)

    if right_answers != -1:
        game_logic.congrats(user_name)
