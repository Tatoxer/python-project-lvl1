from random import randint, choice


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


progr = make_progression()
answer = choice(progr)


def replace_progression(answer, progr):
    i = 0
    while i < (len(progr) - 1):
        if progr[i] == answer:
            progr[i] = ".."
        i += 1
    return progr

