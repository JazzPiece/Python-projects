### 
### Author: Jasur.Jiasuer
### Description: This is a program that let you
###              play Bulls and Cows!! Make sure
###              you guess it right before your
###              opponent!
from os import _exit as exit
print('-----------------------------------------')
print('------- WELCOME TO BULLS AND COWS -------')
print('-----------------------------------------')
first_player = input('Player 1, enter your username:\n')
second_player = input('Player 2, enter your username:\n')

first_code = input(first_player+', enter your code:\n')
if len(first_code) != 3:
    print(first_player+', that code is not valid. Exiting.')
    exit(0)
if first_code.islower() == False:
    print(first_player+', that code is not valid. Exiting.')
    exit(0)
if first_code[0] == first_code[1] or first_code[0] == first_code[2] \
or first_code[1] == first_code[2] :
    print(first_player+', that code is not valid. Exiting.')
    exit(0)
    
second_code = input(second_player+', enter your code:\n')
if len(second_code) != 3:
    print(second_player+', that code is not valid. Exiting.')
    exit(0)
if second_code.islower() == False:
    print(second_player+', that code is not valid. Exiting.')
    exit(0)
if second_code[0] == second_code[1] or second_code[0] == second_code[2] \
or second_code[1] == second_code[2] :
    print(second_player+', that code is not valid. Exiting.')
    exit(0)

index = 0    
while index == 0:
    first_guess = input(first_player+', enter guess:\n')
    if first_guess[0] == second_code[0] and first_guess[1] == second_code[1] \
    and first_guess[2] == second_code[2]:
        print(str(first_player),'wins!')
        exit(0)
    if first_guess[0] != second_code[0] or first_guess[1] != second_code[1] \
    or first_guess[2] != second_code[2]:
        bulls = 0
        cows = 0
        if first_guess[0] == second_code[0]:
            bulls += 1
        if first_guess[1] == second_code[1]:
            bulls += 1
        if first_guess[2] == second_code[2]:
            bulls += 1
        if first_guess[0] == second_code[1]:
            cows += 1
        if first_guess[0] == second_code[2]:
            cows += 1
        if first_guess[1] == second_code[2]:
            cows += 1    
        if first_guess[1] == second_code[0]:
            cows += 1
        if first_guess[2] == second_code[0]:
            cows += 1
        if first_guess[2] == second_code[1]:
            cows += 1
        print('  * bulls: '+str(bulls))
        print('  * cows:  '+str(cows))

    second_guess = input(second_player+', enter guess:\n')
    if second_guess[0] == first_code[0] and second_guess[1] == first_code[1] \
    and second_guess[2] == first_code[2]:
        print(str(second_player),'wins!')
        exit(0)
    if second_guess[0] != first_code[0] or second_guess[1] != first_code[1] \
    or second_guess[2] != first_code[2]:
        bulls = 0
        cows = 0
        if second_guess[0] == first_code[0]:
            bulls += 1
        if second_guess[1] == first_code[1]:
            bulls += 1
        if second_guess[2] == first_code[2]:
            bulls += 1
        if second_guess[0] == first_code[1]:
            cows += 1
        if second_guess[0] == first_code[2]:
            cows += 1
        if second_guess[1] == first_code[2]:
            cows += 1
        if second_guess[1] == first_code[0]:
            cows += 1
        if second_guess[2] == first_code[0]:
            cows += 1
        if second_guess[2] == first_code[1]:
            cows += 1
        print('  * bulls: '+str(bulls))
        print('  * cows:  '+str(cows))