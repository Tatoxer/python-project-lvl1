#!/usr/bin/env python3
from random import randint, choice


description = "What is the result of the expression?"


def do_game_logic():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    symbol = choice(["+", "-", "*"])
    question = f'{number_1} {symbol} {number_2}'
    right_answer = calculate(number_1, number_2, symbol)
    return str(question), str(right_answer)


def calculate(number_1, number_2, symbol):
    answer = ""
    if symbol == "+":
        answer = number_1 + number_2
    elif symbol == "-":
        answer = number_1 - number_2
    elif symbol == "*":
        answer = number_1 * number_2
    return answer
