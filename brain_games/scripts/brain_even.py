#!/usr/bin/env python
import prompt
import random
import sys


def welcome_user():
    print('Welcome to the Brain Games!')

def ask_name():
    name = input('May I have your name? ')
    return name

def greet_user(name):
    print('Hello,', name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

def generate_random_num():
    return random.randint(1, 20)

def question(num):
    print('Question: ', num)

def get_answer():
    answer = input('Your answer: ')
    return answer

def congratulate_user(name):
    print(f'Congratulations, {name}!')
    sys.exit()

# answer_defs
def yes_answer_check(answer, name):
    if answer.lower() == answer:  # если пользователь ответил yes
        print('Correct!')
    else:
        print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
        print('Let''s try again, ', name + '!')
        sys.exit()

def no_answer_check(answer, name):
    if answer.lower() == answer:  # если пользователь ответил no
        print('Correct!')
    else:
        print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
        print('Let''s try again, ', name + '!')
        sys.exit()


def main():
    welcome_user()
    user_name = ask_name()
    greet_user(user_name)
    i = 1
    while i <= 3:
        random_number = generate_random_num()
        question(random_number)
        user_answer = get_answer()
        if random_number % 2 == 0:
            yes_answer_check(user_answer, user_name)
        else:
            no_answer_check(user_answer, user_name)
        i += 1
    congratulate_user(user_name)


main()


if __name__ == '__ main__':
    main()
