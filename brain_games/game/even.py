#!/usr/bin/env python3
from random import randint


rules = "Answer 'yes' if number even otherwise answer 'no'"


def logic():
    question = randint(0, 100)
    if question % 2 == 0:
        right_answer = "yes"
    else:
        right_answer = "no"
    return str(question), right_answer
