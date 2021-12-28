import random
TASK = 'What number is missing in the progression?'


def get_progression(start_number, step, length_of_progression):
    result = [start_number]
    x = 0
    while x < length_of_progression:
        start_number += step
        result.append(start_number)
        x = x + 1
    return result


def generate_round():
    start_number = random.randint(1, 50)
    step = random.randint(1, 10)
    length_of_progression = random.randint(6, 9)
    progression = get_progression(start_number, step, length_of_progression)
    index = random.randint(0, length_of_progression)
    answer = progression[index]
    progression[index] = '..'
    question = ' '.join(map(str, progression))
    return question, answer
