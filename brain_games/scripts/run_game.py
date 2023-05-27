#!/usr/bin/env python
from brain_games.engine import play_solo, play_together
from brain_games.games import calс, even_or_odd, gcd  # add games which u want to play
from brain_games.scripts import get_players


def main():
    greet()
    x = get_players.get_players_info()
    if x[0] == 1:  # solo mode
        points = {
            'calc': play_solo(calс)['points'],
            'even_or_odd': play_solo(even_or_odd)['points'],
            'gcd': play_solo(gcd)['points'],
        }
        result = sum(points.values())
        print(f'Finally you reached {result} points!!!')
        print('Game finished!')
    else:
        p1_name = x[1]
        p2_name = x[2]
        results = {
            'calc': play_together(calс),
            'even_or_odd': play_together(even_or_odd),
            'gcd': play_together(gcd),
            'p1_name': p1_name,
            'p2_name': p2_name,
        }

        print(results)

        # flake8: noqa W503
        p1_summary_points = (
                results['calc']['player1_data']['points'] +
                results['even_or_odd']['player1_data']['points'] +
                results['gcd']['player1_data']['points']
        )

        p2_summary_points = (
                results['calc']['player2_data']['points'] +
                results['even_or_odd']['player2_data']['points'] +
                results['gcd']['player2_data']['points']
        )

        print(f"Summary for ({results['p1_name']}) player:\n"
              f"Points in 'calc' game: {results['calc']['player1_data']['points']}\n"
              f"Points in 'even_or_odd' game: {results['even_or_odd']['player1_data']['points']}\n"
              f"Points in 'gcd' game: {results['gcd']['player1_data']['points']}\n"
              )

        print(f"Summary for ({results['p2_name']}) player:\n"
              f"Points in 'calc' game: {results['calc']['player2_data']['points']}\n"
              f"Points in 'even_or_odd' game: {results['even_or_odd']['player2_data']['points']}\n"
              f"Points in 'gcd' game: {results['gcd']['player2_data']['points']}\n"
              )

        print(f'{results["p1_name"]} points in games: {p1_summary_points}')
        print(f'{results["p2_name"]} points in games: {p2_summary_points}')

        if p1_summary_points > p2_summary_points:
            print(f'{results["p1_name"]} is WINNER!')
        else:
            print(f'{results["p2_name"]} is WINNER!')


def greet():
    print('Hello!')
    return


if __name__ == '__main__':
    main()
