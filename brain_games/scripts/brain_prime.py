import random
import sys


def welcome_user():
    print('Welcome to the Brain Games!')


def ask_name():
    name = input('May I have your name? ')
    return name


def greet_user(name):
    print('Hello, ', name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def generate_random_num():
    return random.randint(2, 15)


def question(num):
    print(f'Question: {num}')


def check_random_num_is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        # print(" # Число простое")
        return True
    else:
        # print(" # Число не является простым")
        return False


def get_answer():
    answer = input('Your answer: ')
    return answer


def congratulate_user(name):
    print(f'Congratulations, {name}!')


def main():
    welcome_user()
    user_name = ask_name()
    greet_user(user_name)
    i = 1
    while i <= 3:
        random_number = generate_random_num()
        question(random_number)
        is_prime = check_random_num_is_prime(random_number)
        user_answer = get_answer()

        if user_answer == 'yes':
            if is_prime is True:
                print('Correct!')
            else:
                print('\'yes\' is wrong answer ;(. Correct answer was \'no\'')  # noqa: E501
                print('Let''s try again, ', user_name + '!')
                sys.exit()
        else:
            if is_prime is False:
                print('Correct!')
            else:
                print('\'no\' is wrong answer ;(. Correct answer was \'yes\'')  # noqa: E501
                print('Let''s try again, ', user_name + '!')
                sys.exit()
        i += 1
    congratulate_user(user_name)


main()

if __name__ == '__main__':
    main()
