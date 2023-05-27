#!usr/bin/env python3
from brain_games.engine import play_solo, play_together
from brain_games.scripts.get_players import get_players_info
from brain_games.games import calс


def solo_game(calc):
    player_data = get_players_info()
    player_name = player_data[1]
    print(f"Good luck, {player_name}!")
    solo_results = play_solo(calc)
    print(f'Your pts in this game: {solo_results}')
    return solo_results


def together_game(game):
    players_data = get_players_info()
    player1_name = players_data[1]
    player2_name = players_data[2]
    together_results = play_together(game)
    return together_results
