#!/usr/bin/env python
import random
import sys


def welcome_user():
    print('Welcome to the Brain Games!')


def ask_name():
    name = input('May I have your name? ')
    return name


def greet_user(name):
    print('Hello,', name + '!')
    print('What is the result of the expression?')


def generate_random_num():
    return random.randint(1, 20)


def generate_random_operation(operations):
    return random.choice(operations)


def question(num1, operation, num2):
    print('Question:', num1, operation, num2)


def get_answer():
    answer = int(input('Your answer: '))  # noqa: E501
    # print(type(answer))
    return answer


def congratulate_user(name):
    print(f'Congratulations, {name}!')
    sys.exit()


# answer_defs
def answer_check(answer, result, name):
    if answer == result:  # если пользователь ответил yes
        print('Correct!')
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {result}')
        print(f'Let\'s try again, {name}!')
        sys.exit()


def main():
    welcome_user()
    user_name = ask_name()
    greet_user(user_name)
    operations = ['+', '-', '*']
    i = 1
    while i <= 3:
        random_number1 = generate_random_num()
        random_number2 = generate_random_num()
        random_operation = generate_random_operation(operations)
        # print('Случайная операция: ', random_operation)
        # print('random_number1 - ', random_number1)
        # print('random_number2 - ', random_number2)
        question(random_number1, random_operation, random_number2)
        user_answer = get_answer()
        if random_operation == '-':
            result = random_number1 - random_number2
            answer_check(user_answer, result, user_name)
        if random_operation == '+':
            result = random_number1 + random_number2
            answer_check(user_answer, result, user_name)
        if random_operation == '*':
            result = random_number1 * random_number2
            answer_check(user_answer, result, user_name)
        i += 1
    congratulate_user(user_name)


main()


if __name__ == '__ main__':
    main()
