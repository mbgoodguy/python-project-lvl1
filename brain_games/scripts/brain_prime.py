#!/usr/bin/env python3


from brain_games.engine import start_game
from brain_games.games import brain_prime_module


def main():
    start_game(brain_prime_module)  # аргумент - импортированный соответствующий модуль игры  # noqa: E501


if __name__ == '__main__':
    main()
