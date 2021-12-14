#!/usr/bin/env python
import prompt
import random
import sys

yes_answer = 'yes'
no_answer = 'no'
number1 = random.randint(1, 20)  # генерация случайного числа 1
number2 = random.randint(1, 20)  # генерация случайного числа 2
number3 = random.randint(1, 20)  # генерация случайного числа 3


def main():  # noqa: C901
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ', name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    # answer_defs
    def yes_answer_check():
        answer = prompt.string('Your answer: ')
        if answer.lower() == yes_answer:  # если пользователь ответил yes
            print('Correct!')
        else:
            print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
            print('Let''s try again, ', name + '!')
            sys.exit()

    def no_answer_check():
        answer = prompt.string('Your answer: ')
        if answer.lower() == no_answer:  # если пользователь ответил no
            print('Correct!')
        else:
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            print('Let''s try again, ', name + '!')
            sys.exit()

    # question defs
    def question1(number1):
        print('Question: ', number1)
        if number1 % 2 == 0:
            yes_answer_check()
        else:
            no_answer_check()

    def question2(number2):
        print('Question: ', number2)
        if number2 % 2 == 0:
            yes_answer_check()
        else:
            no_answer_check()

    def question3(number3):
        print('Question: ', number3)
        if number3 % 2 == 0:
            yes_answer_check()
        else:
            no_answer_check()

    def even_or_odd():
        question1(number1)
        question2(number2)
        question3(number3)
        print('Congratulations, ', name + '!')

    even_or_odd()
    sys.exit()


main()


if __name__ == '__ main__':
    main()
