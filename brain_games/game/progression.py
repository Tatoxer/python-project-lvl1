#!/usr/bin/env python3
from random import choice, randint


DESCRIPTION = "What number is missing in the progression?"


def generate_game_data():
    start = randint(1, 10)
    difference = randint(1, 10)
    progression_length = randint(8, 12)
    progr = make_progression(start, difference, progression_length)
    correct_answer = choice(progr)
    question = game_question(correct_answer, progr)
    return str(question), str(correct_answer)


def make_progression(start, difference, progression_length):
    progression_ = []
    count = 0

    while count < progression_length:
        progression_.append(start + difference * count)
        count += 1
    return progression_


def game_question(answer, progr):
    count = 0
    while count < len(progr):
        if progr[count] == answer:
            progr[count] = ".."
        count += 1
    return progr
