import random

def guess(x):
    rand_num = random.randint(1, x)
    guess = 0

    while guess != rand_num:
        guess = int(input(f'Guess a number between 1 and {x}: \n'))
        if guess < rand_num :
            print('Sorry, your guess is too low. Guess again')
        elif guess > rand_num :
            print('Sorry, your guess is too high. Guess again')
    print(f'Congrats!!. you guessed the number {rand_num} correctly')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # This could be high as well because low = high
        feedback = input(f'Is {guess} Too high(H), Too low(L) or correct(C) :').lower()
        if feedback == 'h' :
            high = guess - 1
        elif feedback == 'l' :
            low = guess + 1
            
    print(f'YAY!! the computer guessed the number {guess} correctly')

computer_guess(10000)