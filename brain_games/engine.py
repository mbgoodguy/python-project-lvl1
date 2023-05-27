import prompt
ROUNDS = 3


def play_together(game_module):
    p1 = play_solo(game_module)
    print('NOW THE NEXT PLAYER!')
    p2 = play_solo(game_module)
    results_from_together = {'player1_data': p1, 'player2_data': p2}
    return results_from_together


#  LOGIC FOR SOLO MODE
def play_solo(game_module):
    points = 0
    attempts = 3
    print(game_module.TASK)

    for _ in range(ROUNDS):
        question, answer = game_module.generate_round()
        print(f'New question: {str(question)}')
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) == str(answer):
            print('Correct!')
            points += 1
        else:
            # attempts -= 1
            print(f"{str(user_answer)} is wrong answer ;(. Correct answer was {str(answer)}")
            # print('ATTEMPTS LEFT: ', attempts)

            # if attempts == 0:
            #     print('You have no more attempts! Game is finished for you!')
            #     solo_result = {
            #         'attempts': attempts,
            #         'points': points
            #     }
            #     return solo_result

    solo_result = {
        'points': points,
    }

    return solo_result
