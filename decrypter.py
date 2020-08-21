###
### Author: Jasur.Jiasuer
### Course: CSc 110
### Description: This is a program that reads an encrypted file and decrypts the file
###              by re-assigning the lines in a correct order according to the index
###              file that has the correct order of the lines. 'decrypted.txt' is created.
def decrypt(encrypted_file,index_file,file_list,index_list):
    '''
    This is my decrypt function, this function opens the encrypted 
    and the index file and reassign the correct lines to original_list.
    'decrypted.txt' is created.
    '''
    info = open(encrypted_file,'r')
    file_list = info.readlines()
    index = open(index_file,'r')
    index_list = index.readlines()
    original_list = file_list.copy()
    '''
    This part reassigns the lines in correct order and write the list 
    into a file called 'decrypted.txt'.
    '''
    for i in range(1,len(file_list)+1):
        index = int(index_list[int(i)-1]) - 1
        original_list[index] = file_list[int(i)-1]
    decrypt_file = open('decrypted.txt','w')
    for line in original_list:
        decrypt_file.write(line)
    decrypt_file.close()
def main():
    '''
    This is my main function, this function creates two empty
    list to store the information in the file.
    file_name = the name of the encrypted file.
    index_file = the name of the index file.
    '''
    file_list = []
    index_list = []
    encrypted_file = input('Enter the name of a mixed text file: \n')
    index_file = input('Enter the mix index file: \n')
    decrypt(encrypted_file,index_file,file_list,index_list)
main()