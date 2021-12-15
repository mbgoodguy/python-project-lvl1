#!/usr/bin/env python
import random
import sys

end = 40
unknown_number = '..'
i = 10


def main():  # noqa: C901
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print('Hello,', name + '!')
    # question defs

    def question1():
        start = random.randint(1, 10)
        step = random.randint(2, 5)
        a = [i for i in range(start, end, step)]
        if len(a) > 10:  # оставляем не более 10 элементов в списке
            for x in range(i, len(a)):
                a.pop(i)
        element = random.choice(a)  # Случайный выбранный элемент из списка
        if element in a:
            element_index = a.index(element)
            # print('Индекс случайно выбранного элемента в списке: ', element_index)   # noqa: E501
            a[element_index] = unknown_number
            # print(a)
        print('Question:', " ".join(map(str, a)))
        answer = int(input('Your answer: '))
        if answer != element:
            print(f'{answer} is wrong answer ;(. Correct answer was {element}')  # noqa: E501
            print(f'Let\'s try again, {name}!')
            sys.exit()
        else:
            print('Correct!')

    def question2():
        start = random.randint(1, 10)
        step = random.randint(2, 5)
        a = [i for i in range(start, end, step)]
        element = random.choice(a)
        if len(a) > 10:
            for x in range(i, len(a)):
                a.pop(i)
        element = random.choice(a)
        if element in a:
            element_index = a.index(element)
            a[element_index] = unknown_number
        print('Question:', " ".join(map(str, a)))
        answer = int(input('Your answer: '))
        if answer != element:
            print(f'{answer} is wrong answer ;(. Correct answer was {element}')  # noqa: E501
            print(f'Let\'s try again, {name}!')
            sys.exit()
        else:
            print('Correct!')

    def question3():
        start = random.randint(1, 10)
        step = random.randint(2, 5)
        a = [i for i in range(start, end, step)]
        element = random.choice(a)
        if len(a) > 10:  # оставляем не более 10 элементов в списке
            for x in range(i, len(a)):
                a.pop(i)
        element = random.choice(a)  # Случайный выбранный элемент из списка
        if element in a:
            element_index = a.index(element)
            # print('Индекс случайно выбранного элемента в списке: ', element_index)   # noqa: E501
            a[element_index] = unknown_number
            # print(a)
        print('Question:', " ".join(map(str, a)))
        answer = int(input('Your answer: '))
        if answer != element:
            print(f'{answer} is wrong answer ;(. Correct answer was {element}')  # noqa: E501
            print(f'Let\'s try again, {name}!')
            sys.exit()
        else:
            print('Correct!')

    def progression():  # вызов функции вопроса
        question1()
        question2()
        question3()
        print(f'Congratulations, {name}!')

    progression()
    sys.exit()


main()
if __name__ == '__ main__':
    main()
