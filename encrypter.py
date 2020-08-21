###
### Author: Jasur.Jiasuer
### Course: CSc 110
### Description: This is a program that reads a file and encrypts the file
###              by mixing the lines in a random order, it also creates an
###              index file that has the correct order of the lines.
###              'encrypted.txt' and 'index.txt' are created.
import random
def encrypt(file_name,file_list,index_list):
    '''
    This is my encrypt function. It uses the algorithmto mix 
    the lines and mix the indexes and creates two files for
    encrypted list and index list.
    '''
    '''
    This part of the code opens the file and reads the file and
    creates a list. It also creates an index list corresponding
    to the lines in order.(starting from 1)
    '''
    info = open(file_name,'r')
    for line in info:
        file_list.append(line)
    lines_file = len(file_list)
    i = 1
    while i < (lines_file+1):
        value = str(i)+'\n'
        index_list.append(value)
        i += 1
    '''
    This part of the code uses the algorithm to swaps
    strings in the file_list and swaps the indexes.
    '''
    count = lines_file*5
    while count > 0:
        first_int = random.randint(0,lines_file-1)
        second_int = random.randint(0,lines_file-1)
        first_string = file_list[first_int]
        second_string = file_list[second_int]
        file_list[first_int] = second_string
        file_list[second_int] = first_string
        first_number = index_list[first_int]
        second_number = index_list[second_int]
        index_list[first_int] = second_number
        index_list[second_int] = first_number
        count -= 1
    '''
    This part of the code writes the encrypted information into
    a file and it also writes the corresponding indexes to a file.
    '''
    encrypted = open('encrypted.txt','w')
    for line in file_list:
        encrypted.write(line)
    encrypted.close()
    index_file = open('index.txt','w')
    for line in index_list:
        index_file.write(str(line))
    index_file.close()
def main():
    '''
    This is my main function, this function creates two empty
    list to store the information in the file.
    random.seed(125) is a part of the algorithm to encrypt the file.
    file_name = the name of the file to encrypt.
    '''
    index_list = []
    file_list = []
    random.seed(125)
    file_name = input('Enter a name of a text file to mix: \n')
    encrypt(file_name,file_list,index_list)
main()