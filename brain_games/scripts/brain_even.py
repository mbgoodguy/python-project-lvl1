#!/usr/bin/env python
import prompt
import random
import sys

yes_answer = 'yes'
no_answer = 'no'
number1 = random.randint(1, 20) # генерация случайного числа 1
number2 = random.randint(1, 20) # генерация случайного числа 2
number3 = random.randint(1, 20) # генерация случайного числа 3


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ', name + '!')
    print ('Answer "yes" if the number is even, otherwise answer "no".')
    
    def even_or_odd():
        question1()
        if number1 % 2 == 0: # проверка если случайное число 1 делится на 2 без остатка
            yes_answer_check()
        else:
            no_answer_check()
        question2()
        if number2 % 2 == 0: # проверка если случайное число 2 делится на 2 без остатка
            yes_answer_check()
        else:
            no_answer_check()
        question3()
        if number3 % 2 == 0: # проверка если случайное число 3 делится на 2 без остатка
            yes_answer_check()
        else:
            no_answer_check()
        print('Congratulations, ', name + '!')    


    # question defs
    def question1():
        print('Question: ', number1)


    def question2():
        print('Question: ', number2)


    def question3():
        print('Question: ', number3)


    # answer_defs
    def yes_answer_check():
        answer = prompt.string('Your answer: ')
        if answer.lower() == yes_answer: # проверка если пользователь ответил yes
                print('Correct!')
        else: 
                print(f'{no_answer} is wrong answer ;(. Correct answer was {yes_answer}.')
                print('Let''s try again, ', name + '!')
                sys.exit()


    def no_answer_check():
        answer = prompt.string('Your answer: ')
        if answer.lower() == no_answer: # проверка если пользователь ответил no
                print('Correct!')
        else:
                print(f'{yes_answer} is wrong answer ;(. Correct answer was {no_answer}.')
                print('Let''s try again, ', name + '!')
                sys.exit()

    even_or_odd()


if __name__ == '__ main__':
    main()
