#!/usr/bin/env python3
from random import randint, choice


rules = "What is the result of the expression?"


def logic():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    symbol = generate_rand_symbol()
    question = f'{number_1} {symbol} {number_2}'
    right_answer = do_calc_logic_result(number_1, number_2, symbol)
    return str(question), right_answer


def generate_rand_symbol():
    symbols = ["+", "-", "*"]
    return choice(symbols)


def do_calc_logic_result(number_1, number_2, symbol):
    answer = ""
    if symbol == "+":
        answer = number_1 + number_2
    elif symbol == "-":
        answer = number_1 - number_2
    elif symbol == "*":
        answer = number_1 * number_2
    return str(answer)
