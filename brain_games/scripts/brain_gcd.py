#!/usr/bin/env python
import random
import sys
# import math если через math.gcd(a, b)


def main():  # noqa: C901
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print('Hello, ', name + '!')
    print('Find the greatest common divisor of given numbers.')

    # question defs
    def question():
        number1 = random.randint(1, 50)  # генерация случайного числа 1
        number2 = random.randint(1, 50)  # генерация случайного числа 2
        print(f'Question: {number1} {number2}')
        answer = int(input('Your answer: '))

        # решение по геометрическому алгоритму Евклида
        while number1 != number2:
            if number1 > number2:
                number1 = number1 - number2
            else:
                number2 = number2 - number1

        if answer != number1:
            print(f'{answer} is wrong answer ;(. Correct answer was {number1}')  # noqa: E501
            print('Let''s try again, ', name + '!')
            sys.exit()
        else:
            print('Correct!')

    def gcd():  # вызов функции вопроса
        question()
        question()
        question()
        print('Congratulations, ', name + '!')

    gcd()
    sys.exit()


main()


if __name__ == '__ main__':
    main()
