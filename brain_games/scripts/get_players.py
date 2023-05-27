#!usr/bin/env python3

def get_players_info():
    players = input('How many players will play? 2 players max. Enter count of players: ')
    while players not in ('1', '2'):
        players = input('You can choose only 1 or 2 players. Input 1 or 2: ')

    if players == '1':
        print("You will play in single player mode! You only have 3 attempts.\nTarget: score more points!".upper())
        name = input('Enter your name: ')
        return [1, name]

    if players == '2':
        print("Let's see who is the best brain! Every player has 3 attempts.\n")
        print("TARGET: score more points than the other player!")
        p1_name = input('Enter Player1 name: ')
        p2_name = input('Enter Player2 name: ')
        print(f'{p1_name} starts first!')
        return [2, p1_name, p2_name]


if __name__ == '__main__':
    get_players_info()
