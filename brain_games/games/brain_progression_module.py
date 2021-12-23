import random
TASK = 'What number is missing in the progression?'


def generate_progression(number1, step, length_of_progression):
    return [number1 + step * i for i in range(length_of_progression)]


def generate_round():
    start = 1
    end = 50
    step = random.randint(1, 8)
    length_of_progression = 10
    question = ''
    number1 = random.randint(start, end)
    index = random.randint(1, length_of_progression)
    # print('Случ-ый индекс: ', index - 1)
    progression = generate_progression(number1, step, length_of_progression)
    # print(progression)
    for i in range(len(progression)):
        if i == index - 1:
            question += '.. '
            result = str(progression[i])
        else:
            question += str(progression[i]) + ' '
    # print(f'Question: {question}, Result: {result}')
    return question, result
