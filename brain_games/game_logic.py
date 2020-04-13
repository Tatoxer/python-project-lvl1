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


def user_answer(name):
    while True:
        answer = input("Your answer: ")
        if answer.isdigit():
            break
        else:
            print(name.capitalize() + ", you should enter a number")
            continue
    return answer


def rand_symbol():
    symbols = ["+", "-", "*"]
    return choice(symbols)


def cal_logic_result():
    number_1 = generate_random_number()
    number_2 = generate_random_number()

    if number_1 < number_2:
        number_1, number_2 = number_2, number_1

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


def remainder_two_numb(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return str(a)


def check_answer(ua, answer, right_answers):
    if str(ua) == str(answer):
        print("Correct!")
        right_answers += 1
        return right_answers
    else:
        print(str(ua) + " is wrong answer ;(")
        print("Correct answer was " + str(answer) + ". Let's try again")
        return right_answers


def make_progression():
    progression = []
    progression_step = randint(1, 10)

    i = 0
    while i < 11:
        if i == 0:
            progression.append(progression_step)
        else:
            a = progression[i - 1] + progression_step
            progression.append(a)

        i += 1
    return progression


def replace_progression(answer, progr):
    i = 0
    while i < len(progr):
        if progr[i] == answer:
            progr[i] = ".."
        i += 1
    return progr
