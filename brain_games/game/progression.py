#!/usr/bin/env python3
from random import choice, randint


rules = "What number is missing in the progression?"


def logic():
    progr = make_progression()
    right_answer = choice(progr)
    question = replace_progression(right_answer, progr)
    return str(question), str(right_answer)


def make_progression():
    progression_ = []
    progression_step = randint(1, 10)

    i = 0
    while i < 11:
        if i == 0:
            progression_.append(progression_step)
        else:
            a = progression_[i - 1] + progression_step
            progression_.append(a)

        i += 1
    return progression_


def replace_progression(answer, progr):
    i = 0
    while i < len(progr):
        if progr[i] == answer:
            progr[i] = ".."
        i += 1
    return progr
