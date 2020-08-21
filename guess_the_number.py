### 
### Author: Jasur.Jiasuer
### Description: This is a simple number guessing
###              game, you have two tries, use them
###              wisely!
from os import _exit as exit
N = input('Enter number to be guessed between 1 and 100, inclusive:\n')
if N.isnumeric() != True:
    print(N+' is not an acceptable value.')
    exit(0)
while int(N) > 100 or int(N) < 1:
    print(N+' is not 1-100, inclusive.')
    N = input('Enter number to be guessed between 1 and 100, inclusive:\n')

N = int(N)
next_guess = input('Enter guess 0:\n')
next_guess = int(next_guess)
guess_total = 0
if next_guess == N:
    print(next_guess,'is correct! Ending game.')
    print('You used',guess_total,'guesses to get the correct solution.')
    print('The correct number was',N)
    exit(0)
while next_guess != N:   
    guess_total = guess_total + 1
    print(next_guess,'is incorrect. Guess again.')
    next_guess = input('Enter guess '+str(guess_total)+':\n')
    next_guess = int(next_guess)
    if next_guess == N:
        print(next_guess,'is correct! Ending game.')
        print('You used',str(guess_total),'guesses to get the correct solution.')
        print('The correct number was',str(N)+'.')
        exit(0)