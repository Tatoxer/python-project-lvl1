#!/usr/bin/env python3
from random import randint, choice
import prompt


def welcome_to_game():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = prompt.string("May I have your name?\n")
    print('Hello, ' + name.capitalize() + "!\n")
    return name


def rules_of_game(rules):
    print(rules)


def is_divide_by_2(number):
    """Check multiplicity of 2"""
    if number % 2 == 0:
        answer = "yes"
        return answer
    else:
        answer = "no"
        return answer


def generate_random_number():
    return randint(0, 100)


def user_answer():
    answer = input("Your answer: ")
    return answer


def rand_symbol():
    symbols = ["+", "-", "*"]
    return choice(symbols)


def cal_logic_result():
    number_1 = generate_random_number()
    number_2 = generate_random_number()
    symbol = rand_symbol()
    answer = ""
    if symbol == "+":
        answer = number_1 + number_2
    elif symbol == "-":
        answer = number_1 - number_2
    elif symbol == "*":
        answer = number_1 * number_2

    print("Question: " + str(number_1) + " " + symbol + " " + str(number_2))
    return int(answer)


def congrats(name):
    print("Congratulations, " + name.capitalize() + "!")
