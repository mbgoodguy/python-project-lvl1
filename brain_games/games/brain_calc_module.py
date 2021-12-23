import random
TASK = "What is the result of the expression?"


def answer_check(random_number1, random_operation, random_number2):
    if random_operation == '+':
        return random_number1 + random_number2
    if random_operation == '-':
        return random_number1 - random_number2
    if random_operation == '*':
        return random_number1 * random_number2


def generate_round():
    operations = ['+', '-', '*']
    random_number1 = random.randint(1, 20)
    random_number2 = random.randint(1, 20)
    random_operation = random.choice(operations)
    question = f"{random_number1} {random_operation} {random_number2}"
    answer = answer_check(random_number1, random_operation, random_number2)  # noqa: E501
    return question, str(answer)

