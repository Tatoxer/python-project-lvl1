#!/usr/bin/env python3
from random import randint


description = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def do_game_logic():
    question = randint(1, 100)
    if is_prime(question):
        right_answer = "yes"
    else:
        right_answer = "no"

    return str(question), right_answer


def is_prime(number):
    count = number // 2 + 1
    while number % count != 0:
        count -= 1
        if count == 1:
            return True
