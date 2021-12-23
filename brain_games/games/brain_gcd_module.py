import random

TASK = 'Find the greatest common divisor of given numbers.'


def generate_round():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    answer = gcd(number1, number2)  # в функцию gcd подставляем аргументы из функции begin_round()   # noqa: E501
    question = f'{number1} {number2}'
    return question, str(answer)


def gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1
    return number1 + number2
