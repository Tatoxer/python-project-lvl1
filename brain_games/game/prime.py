#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def generate_game_data():
    question = randint(1, 100)
    if is_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"

    return str(question), correct_answer


def is_prime(number):
    if number == 1:
        return True

    count = 2
    while number % count != 0:
        if count > number // 2:
            break

        count += 1
        if count > number // 2:
            return True
