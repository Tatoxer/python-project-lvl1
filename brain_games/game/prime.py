#!/usr/bin/env python3
from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def logic():
    question = randint(1, 100)
    right_answer = is_prime(question)
    return str(question), right_answer


def is_prime(number):
    n = number - 1
    while number % n != 0:
        n -= 1
    if n == 1:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
