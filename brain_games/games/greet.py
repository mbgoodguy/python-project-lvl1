import prompt


def get_players():
    players = prompt.integer('How many players will play? 2 players max.\nEnter count of players: ')
    while players <= 0 or players > 2:
        players = prompt.integer('You can choice only 1 or 2 players. Input 1 or 2: ')

    if players == 1:
        print("You will play in single player mode! You only have 3 attempts.\nTarget: score more points!".upper())
        name = prompt.string('Enter your name: ')
        print(f"Good luck, {name}!")
        return [1, name]

    if players == 2:
        print("Let's see who is the best brain!\nEvery player has 3 attempts.\nTarget: score more points than other player!".upper())
        p1_name = prompt.string('Enter Player1 name: ')
        p2_name = prompt.string('Enter Player2 name: ')
        print(f'{p1_name} starts first! Good luck {p1_name}!')
        return [2, p1_name, p2_name]
