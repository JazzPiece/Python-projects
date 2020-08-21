''' Name  : huffman.py
    Author: Jasur.Jiasuer
    Course: CSc 120
    Description: This is a program that reads a file contain preorder
                 traversal and the inorder traversal of the tree and construct
                 the tree. It also print out the tree in postorder and
                 prints the tree out with Huffman Coding.'''
from sys import *
class BinaryTree:
    def __init__(self):
        '''Initialize tree's value, left, right to None'''
        self._value = None
        self._left = None
        self._right = None
    def build_tree(self,pre_order,in_order):
        '''This my recursive method that takes two lists of integers;
        the preorder traversal and the inorder traversal of the
        tree and returns the tree
        parameter: pre_order: list of int in pre order
                   in_order: list of int in in order'''
        if (pre_order == [] or in_order == []):
            #base case
            return None
        else:
            head = pre_order[0]
            head_index = in_order.index(head)
            #set value
            self._value = head
            if len(pre_order[1:1+head_index]) > 0:
                #set left value
                self._left = BinaryTree()
                self._left.build_tree(pre_order[1:1+head_index],in_order[:head_index])
            if len(pre_order[head_index+1:]) > 0:
                #set right value
                self._right = BinaryTree()
                self._right.build_tree(pre_order[head_index+1:],in_order[head_index+1:])

    def print_post(self,post):
        '''This my recursive method print_post that adds
        the postorder traversal of the tree you build from
        the first two lines of the data file to post list
        parameter: post: an empty list
        post-condition: post: list of integers in postorder'''
        if self._value == None:
            #base case
            return
        #Go Left
        if self._left != None:
            self._left.print_post(post)
        #Go Right
        if self._right != None:
            self._right.print_post(post)
        #Add value
        post.append(self._value)

    def __str__(self):
        '''Returns a string representation of the tree.'''
        if self._value == "None":
            return None
        return "({:} {} {})".format(self._value, str(self._left), str(self._right))

def read_file(info):
    '''this is my read_file function that takes file info\
    and returns preorder inorder and sequence lists
    parameter: info: information in file in list
    return values: pre_order: list of integers in preorder
                   in_order: list of integers in inorder
                   sequence: list with string in huffman sequence'''
    file_info = []
    for line in info:
        line = line.split()
        file_info.append(line)
    pre_order = file_info[0]
    in_order = file_info[1]
    sequence = file_info[2]
    return pre_order,in_order,sequence

def decode(Tree,Root,seq):
    '''this is my decode function that takes decodes
    the Tree with Huffman Coding and returns a string
    parameter: Tree: BinaryTree object
               seq: string of encoded sequence of values
               Root: BinaryTree object representing the root of the BinaryTree'''
    if len(seq) > 0:
        if Tree._left == None and Tree._right == None:
            return (str(Tree._value) + decode(Root,Root,seq))
        elif seq[0] == '0':
            if Tree._left == None:
                return decode(Root,Root,seq[1:])
            else:
                return decode(Tree._left,Root,seq[1:])
        elif seq[0] == '1':
            if Tree._right == None:
                return decode(Root,Root,seq[1:])
            else:
                return decode(Tree._right,Root,seq[1:])
    elif Tree._left == None and Tree._right == None:
        return str(Tree._value)
    else:
        return ''
def main():
    T = BinaryTree()
    file = input('Input file: ')
    try:
        info = open(file)
    except:
        print("ERROR: Could not open file " + file)
        exit(1)
    pre_order,in_order,sequence = read_file(info)
    T.build_tree(pre_order,in_order)
    post = []
    T.print_post(post)
    print(' '.join(post))
    #Decoding
    sequence = sequence[0]
    print(decode(T,T,sequence))
main()