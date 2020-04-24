from random import randint


DESCRIPTION = "Answer 'yes' if number even otherwise answer 'no'"


def generate_game_data():
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return str(question), correct_answer
