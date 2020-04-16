#!/usr/bin/env python3
from random import choice, randint


description = "What number is missing in the progression?"


def do_game_logic():
    progr = make_progression()
    right_answer = choice(progr)
    question = replace_progression(right_answer, progr)
    return str(question), str(right_answer)


def make_progression():
    start = randint(1, 10)
    difference = randint(1, 10)
    progression_ = []
    count = 0
    while count < randint(8, 12):
        progression_.append(start + difference * count)
        count += 1
    return progression_


def replace_progression(answer, progr):
    i = 0
    while i < len(progr):
        if progr[i] == answer:
            progr[i] = ".."
        i += 1
    return progr
