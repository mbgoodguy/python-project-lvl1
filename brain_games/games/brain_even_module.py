import random
TASK = "Answer 'yes' if the number is even, otherwise answer 'no'."


def generate_round():
    num = random.randint(0, 30)
    answer = 'yes' if is_even(num) is True else 'no'
    return str(num), answer


def is_even(num):
    return True if num % 2 == 0 else False
