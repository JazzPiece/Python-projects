''' Name  : huffman.py
    Author: Jasur.Jiasuer
    Course: CSc 120
    Description: This is a program called writer-bot that will use the markov
                    chain algorithm to read in a file and create a text.'''
import sys
import random
SEED = 8
NONWORD = "@"
random.seed(SEED)

class Hashtable:
    def __init__(self,m):
        '''Initialize the underlying Python list implementing
        the hash table and size
        parameter: m = size of hashtable'''
        self._pair = [None]*m
        self._size = m

    def put(self, key, value):
        '''this is my put function that hashes key
        and inserts the key/value pair in the hash
        table.
        parameter: key = string, prefix
                   value = list of words, suffixes'''
        hash_v = self._hash(key)
        while self._pair[hash_v] != None:
                hash_v -= 1
        self._pair[hash_v] = [key,value]

    def get(self, key):
        '''this is my get function that looks up key in the
        hash table and if found, returns the corresonding value.
        If not found, it returns None.
        parameter: key = string, prefix
        returns: list of words, suffixe(s)
                 None if not found
        '''
        hash_v = self._hash(key)
        if self._pair[hash_v] != None:
            while self._pair[hash_v][0] != key:
                hash_v -= 1
            return self._pair[hash_v][1]
        return None

    def __contains__(self,key):
        '''this is my __contains__ method looks up key in the hash table
        and if found returns True and otherwise returns False.
        parameter: key = string, prefix
        returns: True if empty
                 False if not empty
        '''
        hash_v = self._hash(key)
        while self._pair[hash_v] != None:
            if self._pair[hash_v][0] == key:
                return True
            hash_v -= 1
        return False

    def __str__(self):
        '''Returns a string representation of the ADT.'''
        return str(self._pair)
    #taken from spec
    def _hash(self, key):
        p = 0
        for c in key:
            p = 31*p + ord(c)
        return p % self._size

def build_table(info, m, n):
    '''This is my build_table function, this function build a table of
    all of the possible prefix size word prefixes and the suffixes that
    follow in file
    parameters: info = info in file
                n = prefix size
                m = size of ADT
    returns:    hash_t = ADT object with prefixes and suffixes'''
    hash_t = Hashtable(m)
    file_list = []
    #creates items in ADT
    for line in info:
        line = line.strip('\n').split()
        file_list += line
    for i in range(0, len(file_list)):
        key = []
        value = []
        #Creats NONWORD as prefixes
        if i == 0:
            hash_t.put(' '.join([NONWORD, NONWORD]),[file_list[0]])
            hash_t.put(' '.join([NONWORD, file_list[0]]),[file_list[1]])
        #creates the key
        for word in range(i, i+n):
            key.append(file_list[word])
        #breaks the loop if reach the end index
        if len(key) != n:
            pass
        else:
            key_str = ' '.join(key)
            if (i+n) >= len(file_list):
                break
            value.append(file_list[i+n])
            if key_str not in hash_t:
                hash_t.put(key_str,value)
            else:
                val = hash_t.get(key_str)
                val.append(value[0])
    return hash_t

def generate(table, file, text_size, n):
    '''This is my generate function, this function takes in
    the object (table) and finds suffixes for each key
    parameters: table =  ADT object of prefixes and the suffixes
                n = prefix size
                text_size = size of text
                file = file name
    returns:    string = list of words in generated text'''
    info = open(file).readline().split()
    string = info[:n]
    key = info[:n]
    while len(string) < text_size:
        prefix = ' '.join(key)
        suffixes = table.get(prefix)
        if len(suffixes) == 1:
            suffix = suffixes[0]
        else:
            index = random.randint(0,len(suffixes) - 1)
            suffix = suffixes[index]
        string.append(suffix)
        key.append(suffix)
        key = key[1:]
    return string

def print_list(tlist,word_num):
    '''This is my print_list function, it prints of the generated text
    parameters: word_num =  number of words of output
                tlist = list of words in generated text
    '''
    count = 0
    for i in range(word_num):
        if (i-count*10) % 9 == 0 and i != 0:
            print(tlist[i], end = '')
        elif i%10 == 0 and i != 0:
            print('\n', end = '')
            print(tlist[i], end = ' ')
            count += 1
        elif i == word_num-1:
            print(tlist[i]+'\n', end = '')
            break
        else:
            print(tlist[i], end = ' ')
    if word_num % 10 == 0:
        print('\n', end = '')

def main():
    sfile = input()
    m = int(input())
    n = int(input())
    if n < 1:
        print('ERROR: specified prefix size is less than one')
        sys.exit(1)
    info = open(sfile)
    table = build_table(info, m, n)
    #print(table)
    text_size = int(input())
    if text_size < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(1)
    tlist = generate(table, sfile, text_size, n)
    print_list(tlist, text_size)

main()