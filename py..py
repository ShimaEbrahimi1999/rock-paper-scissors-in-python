import random

def start():
    total_score = 0
    while -1 <= total_score < 2:
        key_words = ['scissor', 'paper', 'rock']
        picked_word = random.choice(key_words)
        ask_user = input('rock paper scissor?: ')
        score = 0
        match picked_word, ask_user:
            case ('rock', 'scissor'):
                score -= 1
                print('you lost a point')
            case ('scissor', 'paper'):
                score -= 1
                print('you lost a point')
            case ('paper', 'rock'):
                score -= 1
                print('you lost a point')
            case ('scissor', 'rock'):
                score += 1
            case ('paper', 'scissor'):
                score += 1
            case ('rock', 'paper'):
                score += 1
        total_score += score
        print(f" You've got {total_score}.")
        if total_score == 2:
            print('you won.')
        elif total_score == -2:
            print('you lost.')


user_name = input('what is your name? ')
name = user_name
print(f'''hello {name}. when your score reached 2, \
the game is over and you are the winner. if \
the score reached -2 the pc is the winner.''')

start()

while True:
    start_over = int(input('Do you want to play again? if yes, type 0 if not type 1: '))
    if start_over == 0:
        print('really happy to play with you!')
        start()
    else:
        print('had a nice time with you! I hope you come back soon!  bye.')
        break
