#!/usr/bin/env python3
from brain_games.game_logic import welcome_to_game, welcome_user
from brain_games.game_logic import rules_of_game, generate_random_number
from brain_games.game_logic import is_divide_by_2, user_answer_yes_no, congrats, check_answer_yes_no


def even():
    welcome_to_game()
    name = welcome_user()
    rules_of_game("Answer 'yes' if number even otherwise answer 'no'")
    right_answers = 0

    while right_answers < 3:
        rand_number = generate_random_number()
        answer = is_divide_by_2(rand_number)
        print("Question: " + str(rand_number))
        ua = user_answer_yes_no(name)

        right_answers = check_answer_yes_no(ua, answer, right_answers)

    congrats(name)
