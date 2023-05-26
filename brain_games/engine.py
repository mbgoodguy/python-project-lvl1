import prompt
# import datetime

from .games import greet
ROUNDS = 3


# general game algorithm
def start_game(game):
    players = greet.get_players()
    if players[0] == 1:
        solo_data = play_solo(game)
        solo_pts = get_pts(solo_data)
        return {solo_data, solo_pts}
    else:
        together_data = play_together(game)
        # p1_pts = together_data.get('player1_data').get('points')
        # p2_pts = together_data.get('player2_data').get('points')
        return together_data


def play_solo(game):
    points = 0  # for point system calculate
    attempts = 3
    print(game.TASK)
    # start_time = datetime.datetime.now()  # initialize start_time before for

    for _ in range(ROUNDS):
        question, answer = game.generate_round()
        print(f'New question: {str(question)}')
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) == str(answer):
            print('Correct!')
            points += 1
        else:
            attempts -= 1
            print(f"{str(user_answer)} is wrong answer ;(. Correct answer was {str(answer)}")
            print('ATTEMPTS LEFT: ', attempts)

            if attempts == 0:
                no_attempts()
                player_data = {
                    'attempts': attempts,
                    'points': points
                }
                return player_data

    player_data = {
        'attempts': attempts,
        'points': points,
    }

    return player_data


def play_together(game):
    player1_data = play_solo(game)
    print('NOW THE NEXT PLAYER!')
    player2_data = play_solo(game)
    # p2_points = get_pts(player2_data)  # save points
    # p1_points = get_pts(player1_data)  # save points

    if player1_data.get('attempts') == 0 and player2_data.get('attempts') == 0:
        print('VOT ETO VY CHUDIKI!!! XD')

    return {'player1_data': player1_data, 'player2_data': player2_data}


def no_attempts():
    print('You have no more attempts! Game is finished for you!')


def get_pts(solo_data):
    return solo_data.get('points')


def lose_output():
    print('You lose! Game is finished 4 you!')


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
