from random import randint


DESCRIPTION = "What number is missing in the progression?"


def generate_game_data():
    start = randint(1, 10)
    difference = randint(1, 10)
    progression_length = randint(8, 12)

    progression = make_progression(start, difference, progression_length)
    random_progression_index = randint(0, progression_length - 1)
    correct_answer = progression[random_progression_index]
    question = create_game_question(random_progression_index, progression)

    return str(question), str(correct_answer)


def make_progression(start, difference, progression_length):
    progression_ = []
    count = 0

    while count < progression_length:
        progression_.append(start + difference * count)
        count += 1
    return progression_


def create_game_question(index, progression):
    progression[index] = ".."
    return progression
