#!usr/bin/env python3
from brain_games.engine import play_solo, play_together
from brain_games.scripts.get_players import get_players_info
from brain_games.games import gcd


def main():
    start_game(gcd)


if __name__ == '__main__':
    main()
