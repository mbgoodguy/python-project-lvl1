#!/usr/bin/env python3
from brain_games.engine import start_game
from brain_games.games import progression


def main():
    start_game(progression)  # аргумент - импортированный соответствующий модуль игры  # noqa: E501


if __name__ == '__main__':
    main()
