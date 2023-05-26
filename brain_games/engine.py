import prompt
import datetime
from .scripts import greeting_logic
from .games import greet
ROUNDS = 5


def start_game(game):
    greeting_logic.main()
    players = greet.get_players()

    if players == 1:
        solo_data = play_solo(game)
        print(f'Your pts: {solo_data.get("points")}')
    else:
        together_data = play_together(game)
        print(f'P1 pts: {together_data["p1_points"]}')
        print(f'P2 pts: {together_data["p2_points"]}')


def play_solo(game):
    name = prompt.string('Enter your name: ')
    points = 0  # for point system calculate
    attempts = 3
    print(f"Good luck, {name}! Timer started!")
    print(game.TASK)
    start_time = datetime.datetime.now()

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
                lose_output()
                player_data = {
                    'name': name,
                    'attempts': attempts,
                    'points': points
                }
                return player_data

    time_result = time_calculate(start_time)
    player_data = {
        'name': name,
        'time': time_result,
        'attempts': attempts,
        'points': points,
    }

    return player_data


def play_together(game):
    player1_data = play_solo(game)
    print('NOW THE NEXT PLAYER!')
    player2_data = play_solo(game)
    p2_points = get_pts(player2_data)  # save points
    p1_points = get_pts(player1_data)  # save points

    if player1_data.get('attempts') == 0 and player2_data.get('attempts') == 0:
        print('VOT ETO VY CHUDIKI!!! XD')
    sum_points = {
        'p1_points': p1_points,
        'p2_points': p2_points,
    }
    return sum_points


def time_comparsion(player1, player2):
    if player1.get('time') < player1.get('time'):
        print(f'Player {player2.get("name")} was faster!')
    else:
        print(f'Player {player1.get("name")} was faster!')


def time_formatting(player):
    print(f"Player's {player.get('name')} time: {int(player.get('time')[0])} minutes {int(player.get('time')[1])} seconds ")


def is_no_attempts(attempts):
    if attempts == 0:
        print('You have no more attempts! Game is finished for you!')
        return True
    else:
        print('You have {attempts} attempts!')
        return False


def time_calculate(start_time):
    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    minutes = time_diff.total_seconds() // 60
    seconds = time_diff.total_seconds() % 60
    time_result = [minutes, seconds]

    return time_result


def get_pts(player_data):
    return player_data.get('points')


def lose_output():
    print('You lose! Game is finished 4 you!')
