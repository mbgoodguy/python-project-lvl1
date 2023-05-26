#!/usr/bin/env python

from brain_games.scripts import brain_calc, brain_even, greeting_logic
from brain_games.games import greet


def main():
    greeting_logic.main()
    players = greet.get_players()
    if players[0] == 1:
        even_pts = brain_even.main()
        calc_pts = brain_calc.main()
        pts = calc_pts + even_pts
        print(f'YOUR PTS: {pts}')
    else:
        even_pts = brain_even.main()
        calc_pts = brain_calc.main()
        p1_name = players[1]
        p2_name = players[2]
        print(f"Player {p1_name} has {even_pts['player1_data']['player1_data']['points']}")
        print(f"Player {p2_name} has {even_pts['player2_data']['player2_data']['points']}")


if __name__ == '__main__':
    main()
