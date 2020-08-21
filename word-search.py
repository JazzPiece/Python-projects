### Name:   word_search.py
### Author: Jasur.Jiasuer
### Course: CSc 120
### Description: This is a program Word search , this is a word game that
###              involves searching for words in a (random) grid of letters.           
def occurs_in(s,L):
    '''this fuction return true if string is in word_list'''
    for word in L:
        if s == word:
            return True
            
def horizontal_search(letter_list,word_list):
    '''this function does a horizontal search on a square 2D list
    parameters: letter_list = list of letters
                word_list = list of all the words
    returns:    found_words = list of found words
    pre-condition: all lists
    post-condition: list'''
    poss_words = []
    found_words = []
    '''
    This part creates a list with all possible words
    '''
    for start in range((len(letter_list)+1)):
        for row in range(len(letter_list)):
            for letter in range((len(letter_list)+1)):
                word = letter_list[row][start:letter]
                if len(word) >= 3:
                    word = ''.join(word)
                    poss_words.append(word)
    '''this part return words that are in word_list
    '''
    for word in poss_words:
        if occurs_in(word,word_list):
            found_words.append(word)
    return found_words
    
def make_letter_list(letter_list_name):
    '''this function takes the name of letter_list and turn
    it into a 2D list
    parameters: letter_list_name = name of list of letters
    pre-condition: letter_list_name is a string
    post-condition: list'''
    letter_list = []
    info = open(letter_list_name)
    letter_list_1 = info.readlines()
    for row in letter_list_1:
        row = row.strip('\n').split()
        letter_list.append(row)
    return letter_list
    
def reverse_list(letter_list,found_words,word_list):
    '''this is my function that reverses the grid of letters letter_list
    parameters: letter_list = list of letters
                word_list = list of all the words
                found_words = list of found words
    returns:    found_words = list of found words
    pre-condition: all lists
    post-condition: list'''
    reverse_letter_list = []
    for row in letter_list:
        row_1 = row.copy()
        row_1.reverse()
        reverse_letter_list.append(row_1)
    search_list = horizontal_search(reverse_letter_list,word_list)
    found_words+=search_list
    return found_words

def vertical_list(letter_list,found_words,word_list):
    '''this is my function that makes the grid of letters letter_list vertical
    parameters: letter_list = list of letters
                word_list = list of all the words
                found_words = list of found words
    returns:    found_words = list of found words
    pre-condition: all lists
    post-condition: all lists'''
    vertical_letter_list = []
    for row in range(len(letter_list)):
        column_list = []
        for column in range(len(letter_list)):
            column_list.append(letter_list[column][row])
        vertical_letter_list.append(column_list)
    search_list = horizontal_search(vertical_letter_list,word_list)
    found_words+=search_list
    return found_words,vertical_letter_list
    
def reverse_vertical_list(vertical_letter_list,found_words,word_list):
    '''this function passes vertical_letter_list in to reverse_list function
    to make and search words in reverse_vertical_list
    parameters: vertical_letter_list = list of letters in vertical order
                found_words = list of found words
                word_list = list of all the words
    returns:    found_words = list of found words
    pre-condition: all lists
    post-condition: list'''
    found_words = reverse_list(vertical_letter_list,found_words,word_list)
    return found_words
    
def diag_search(letter_list,found_words,word_list):
    '''this function does a diagonal search on words
    poss_words = list with all offsets of the list
    neg_offset = lowest possible offset
    pos_offset = highest possible offset
    parameters: letter_list = list of letters
                found_words = list of found words
                word_list = list of all the words
    returns:    found_words = list of found words
    pre-condition: all lists
    post-condition: list'''
    poss_words = []
    neg_offset = 0 - (len(letter_list) - 3)
    pos_offset = (len(letter_list) - 2)
    for off in range(neg_offset,pos_offset):
        word = ''
        if off > 0:
            i,j = 0,off
        else:
            i,j = -off,0
        while i < len(letter_list) and j < len(letter_list):
            word += letter_list[i][j]
            i,j = i+1, j+1
        poss_words.append(word)
    '''
    this part of my code looks for words in word_list that is in poss_words
    '''
    for word in word_list:
        for i in poss_words:
            if word in i:
                found_words.append(word)
    return found_words
    
def print_found_words(found_words):
    '''this function sort and prints every word in found words
    parameter: found_words = list of found words
    pre-condition: list
    '''
    found_words.sort()
    for word in found_words:
        print(word)
        
def main():
    '''this is my main function
    word_list_name = word list name, string
    letter_list_name = letter list name, string
    found_words = lists of found words, updated everytime where there's 
    a search '''
    word_list_name = input()
    letter_list_name = input()
    word_list = make_words_list(word_list_name)
    letter_list = make_letter_list(letter_list_name)
    found_words = horizontal_search(letter_list,word_list)
    found_words = reverse_list(letter_list,found_words,word_list)
    found_words,vertical_letter_list = vertical_list(letter_list,found_words,word_list)
    found_words = reverse_vertical_list(vertical_letter_list,found_words,word_list)
    found_words = diag_search(letter_list,found_words,word_list)
    print_found_words(found_words)
    
def make_words_list(word_list_name):
    '''this function reads in the word file and turn it into a list
    parameters: word_list_name = name of list of all the words
    pre-condition: word_list_name is a string
    post-condition: list'''
    word_list = []
    info = open(word_list_name)
    word_list_1 = info.readlines()
    for word in word_list_1:
        word = word.strip('\n').lower()
        word_list.append(word)
    return word_list
    
main()