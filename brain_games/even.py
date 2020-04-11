#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user


def even():
    print("Welcome to the Brain Games!\nAnswer 'yes' if number even otherwise answer 'no'")
    name = welcome_user()
    right_answers = 0
    used_numbers = []

    while right_answers < 3:
        rand_number = randint(0, 100)

        for i in used_numbers:
            if i in used_numbers:
                rand_number = randint(0, 100)

        used_numbers.append(rand_number)

        if rand_number % 2 == 0:
            answer = "yes"
        else:
            answer = "no"

        print("Question: " + str(rand_number))
        user_answer = input("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            right_answers += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, ")

    print("Congratulations, " + name + "!")
