from brain_games.engine import start_game
from brain_games.games import calс


def main():
    start_game(calс)
    # def time_formatting():
    #     minutes = time_calculate(start_time).get('minutes')
    #     seconds = time_calculate(start_time).get('seconds')
    #     return f"Player's {play_solo(game).get('name')} time: {minutes} minutes {seconds} seconds"

    # def time_calculate(start_time):
    #     end_time = datetime.datetime.now()
    #     time_diff = end_time - start_time
    #     minutes = time_diff.total_seconds() // 60
    #     seconds = time_diff.total_seconds() % 60
    #     time_result = {
    #         'minutes': minutes,
    #         'seconds': seconds,
    #     }
    #
    #     return time_result

    # def time_comparsion(player1, player2):
    #     if player1.get('time') < player1.get('time'):
    #         print(f'Player {player2.get("name")} was faster!')
    #     else:
    #         print(f'Player {player1.get("name")} was faster!')

    #                 time_result = time_formatting(time_calculate(start_time))


if __name__ == '__main__':
    main()
