#!/usr/bin/env python
import random
import sys

operations = ['+', '-', '*']


def main():  # noqa: C901
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print('Hello, ', name + '!')
    print('What is the result of the expression?')

    # question defs
    def question():
        number1 = random.randint(1, 20)  # генерация случайного числа 1
        number2 = random.randint(1, 20)  # генерация случайного числа 2
        summ = number1 + number2
        difference = number1 - number2
        multiply = number1 * number2
        random_operation = random.choice(operations)
        print(f'Question: {number1} {random_operation} {number2}')
        if random_operation == '+':
            answer = int(input('Your answer: '))
            if answer != number1 + number2:
                print(f'{answer} is wrong answer ;(. Correct answer was {summ}')  # noqa: E501
                print('Let''s try again, ', name + '!')
                sys.exit()
            else:
                print('Correct!')
        if random_operation == '-':
            answer = int(input('Your answer: '))
            if answer != number1 - number2:
                print(f'{answer} is wrong answer ;(. Correct answer was {difference}')  # noqa: E501
                print('Let''s try again, ', name + '!')
                sys.exit()
            else:
                print('Correct!')
        if random_operation == '*':
            answer = int(input('Your answer: '))
            if answer != number1 * number2:
                print(f'{answer} is wrong answer ;(. Correct answer was {multiply}')  # noqa: E501
                print('Let''s try again, ', name + '!')
                sys.exit()
            else:
                print('Correct!')

    def calc():  # вызов функции вопроса
        question()
        question()
        question()
        print('Congratulations, ', name + '!')

    calc()
    sys.exit()


main()


if __name__ == '__ main__':
    main()
