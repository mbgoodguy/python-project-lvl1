#!/usr/bin/env python


from brain_games.engine import start_game
from brain_games.games import brain_even_module


def main():
    start_game(brain_even_module)  # аргумент - импортированный соответствующий модуль игры  # noqa: E501


if __name__ == '__main__':
    main()
