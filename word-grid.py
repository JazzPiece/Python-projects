import random
### Name:   word_grid.py
### Author: Jasur.Jiasuer
### Course: CSc 120
### Description: This is a program that creates a word list 
###              file.
###              
def print_grid(out_list):
    '''this is my print grid function, it takes the 2D list of
    letters and print it out
    parameter: out_list = list of letters, 2D
    pre-condition: out_list must be a 2D list of letter'''
    for lists in out_list:
        i = 0
        while i < len(lists):
            if i == (len(lists)-1):
                print(lists[i])
            else:
                print(lists[i]+',',end='')
            i += 1
def make_grid(N):
    '''this function make a grid of letters
    parameter: N = grid size
    pre-condition: N must be an int
    post-condition: The return value is a list
    '''
    out_list = []
    for i in range(N):
        grid_list = []
        for j in range(N):
            number = random.randint(97,122)
            grid_list.append(chr(number))
        out_list.append(grid_list)
    return out_list
def main():
    '''
    N = grid size
    S = seed value
    '''
    N = int(input())
    S = input()
    random.seed(S)
    out_list = make_grid(N)
    print_grid(out_list)
main()