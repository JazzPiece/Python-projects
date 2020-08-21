###
### Author: Jasur.Jiasuer
### Course: CSc 110
### Description: This is a program that manage your contacts!
###              enter 'add contact' to add contact; to show contact, enter
###              'show contacts with name/email/phone name/email/phone'
###              enter 'exit' to exit the program! 
###              autosaves in contacts.txt
def load(all_info):
    '''
    This function loads everything in the 'contacts.txt' file
    and add them into my set all_info
    '''
    info = open('contacts.txt','r')
    for line in info:
        line_list = line.rstrip('\n').split(' | ')
        line_tuple = tuple(line_list)
        all_info.add(line_tuple)
def main():
    '''
    This is my main function, it creates an empty 
    set and calls load and ask_user functions
    '''
    all_info = set()
    print('Welcome to the contacts app!')
    load(all_info)
    ask_user(all_info)
def show_contact(user_input,all_info):
    '''
    This is my show_contact function that takes user input
    and looks for the contact that matches with user input
    or return 'None'
    '''
    count = 0
    '''
    This part changes user_input so that it matches the items
    in tuples in all_info
    '''
    input_list = user_input.split(' ')
    index = input_list.index('with')
    contact = str(' '.join(input_list[(index+2):]))
    for info in all_info:
        if contact in info:
            info_list = list(info)
            print(str(info_list[0])+"'s",'contact info:')
            print('  email:',info_list[1])
            print('  phone:',info_list[2])
        else:
            count += 1
    '''
    if count is equals to the length of the set(all_info)
    that means the if statement is not executed, hence
    no item in all_info matches contact
    '''
    if count == len(all_info):
        print('None')
def add_contact(all_info):
    '''
    This is my add_contact function, this function takes
    user input for name, email, phone and add it into all_info
    '''
    name = input('name:\n')
    email = input('email:\n')
    phone = input('phone:\n')
    contact_list = tuple([name,email,phone])
    if contact_list in all_info:
        print('Contact already exists!')
    else:
        all_info.add(contact_list)
        print('Contact added!')
        '''
        This part of my code saves the set into contact.txt
        because you are only changing the file if you're adding
        a contact
        '''
        info = open('contacts.txt','w')
        for line in all_info:
            line_list = ' | '.join(list(line))+'\n'
            info.write(line_list)
        info.close()
def ask_user(all_info):
    '''
    This is my ask_user function, it asks for user input
    untill user has entered 'exit'
    user_input = can only be 'add contact',
    'show contacts with name/email/phone name/email/phone'
    and 'exit'. anything else the function will return 'Huh?'
    '''
    while True:
        user_input = str(input('>\n'))
        if user_input == 'add contact':
            add_contact(all_info)
        elif user_input.startswith('show contacts with'):
            show_contact(user_input,all_info)
        elif user_input == 'exit':
            print('Goodbye!')
            break
        else:
            print('Huh?')
main()