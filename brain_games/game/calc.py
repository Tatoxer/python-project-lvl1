#!/usr/bin/env python3
from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def generate_game_data():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    operation = choice(["+", "-", "*"])
    question = f'{number_1} {operation} {number_2}'
    correct_answer = calculate(number_1, number_2, operation)
    return str(question), str(correct_answer)


def calculate(number_1, number_2, symbol):
    answer = ""
    if symbol == "+":
        answer = number_1 + number_2
    elif symbol == "-":
        answer = number_1 - number_2
    elif symbol == "*":
        answer = number_1 * number_2
    return answer
