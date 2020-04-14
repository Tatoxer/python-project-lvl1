#!/usr/bin/env python3
from random import randint


rules = "Find the greatest common divisor of given numbers."


def logic():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = f'{str(number_1)} {str(number_2)}'
    right_answer = remainder_two_numb(number_1, number_2)
    return str(question), right_answer


def remainder_two_numb(number_1, number_2):
    if number_1 < number_2:
        number_1, number_2 = number_2, number_1

    while number_2 != 0:
        remainder = number_1 % number_2
        number_1 = number_2
        number_2 = remainder
    return str(number_1)
