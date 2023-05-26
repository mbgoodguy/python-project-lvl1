import prompt


def get_players():
    players = prompt.integer(
        'How many players will play? 2 players max.\nEnter count of players: '
    )
    while players <= 0 or players > 2:
        players = prompt.integer('You can choice only 1 or 2 players. Input count of players: ')
    if players == 1:
        print("Ok! You'll play in solo-mode! The game will end if you make 3 mistakes :)".upper())
    if players == 2:
        print("Fine! Let's see who is the best brain!\n"
              "Every player has 3 attempts. If a player runs out of attempts, the game is over for him")
    return players
