import random
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    divisor = 2
    if num <= 1:
        return False
    while divisor <= num / 2:
        if num % divisor == 0:
            return False
            break
        else:
            divisor += 1
    return True


def generate_round():
    num = random.randint(1, 13)
    if is_prime(num):
        return str(num), 'yes'
        return str(num), 'no'
