import prompt
ROUNDS = 3


def start_game(game):  # в качестве аргумента выступают имена игровых модулей в скриптах, например brain_prime_module  # noqa: E501
    print("Welcome to The Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.TASK)
    start_from_round = 1

    for start_from_round in range(ROUNDS):
        question, answer = game.generate_round()  # получение значений из модуля игры  # noqa: E501
        print("Question: " + question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {answer}")  # noqa: E501
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
