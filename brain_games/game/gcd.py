#!/usr/bin/env python3
from random import randint


DESCRIPTION = "Find the greatest common divisor of given numbers."


def generate_game_data():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = f'{str(number_1)} {str(number_2)}'
    correct_answer = get_gcd(number_1, number_2)
    return str(question), str(correct_answer)


def get_gcd(number_1, number_2):
    if number_1 < number_2:
        number_1, number_2 = number_2, number_1

    while number_2 != 0:
        remainder = number_1 % number_2
        number_1 = number_2
        number_2 = remainder
    return number_1
