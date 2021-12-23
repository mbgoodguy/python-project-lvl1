#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games import brain_progression_module


def main():
    start_game(brain_progression_module)  # аргумент - импортированный соответствующий модуль игры  # noqa: E501


if __name__ == '__ main__':
    main()
