#!/usr/bin/env python3
from random import randint


description = "Answer 'yes' if number even otherwise answer 'no'"


def do_game_logic():
    question = randint(1, 100)
    if question % 2 == 0:
        right_answer = "yes"
    else:
        right_answer = "no"
    return str(question), right_answer
