import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Apolodizem, guess again. Its too low')
        elif guess > random_number:
            print('Apologize, guess again. Its too high')

    print(f'Yay, Congrats. You have guessed the number {random_number} correctly.')

guess(10)    