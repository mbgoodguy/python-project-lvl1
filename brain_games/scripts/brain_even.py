#!/usr/bin/env python


from brain_games.engine import start_game
from brain_games.games import even_or_odd


def main():
    start_game(even_or_odd)


if __name__ == '__main__':
    main()
