#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user


def is_divide_by_2(number):
    """Check multiplicity of 2"""
    if number % 2 == 0:
        return True
    else:
        return False


def rand_numbers():
    """Generate random number from 0 to 100"""
    used_numbers = []
    rand_number = randint(0, 100)

    for i in used_numbers:
        if i in used_numbers:
            rand_number = randint(0, 100)

    used_numbers.append(rand_number)
    return rand_number


def even():
    print("Welcome to the Brain Games!")
    print("Answer 'yes' if number even otherwise answer 'no'")
    name = welcome_user()
    right_answers = 0

    while right_answers < 3:
        rand_number = rand_numbers()
        if is_divide_by_2(rand_number) is True:
            answer = "yes"
        else:
            answer = "no"

        print("Question: " + str(rand_number))
        user_answer = input("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            right_answers += 1
        else:
            print("'yes' is wrong answer ;(")
            print("Correct answer was 'no'. Let's try again")

    print("Congratulations, " + name.capitalize() + "!")
