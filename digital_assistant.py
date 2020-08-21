###
### Author: Jasur.Jiasuer
### Course: CSc 110
### Description: This is a Digital Assistant(DA) program! You can tell the DA something and it 
###              will remember it and tell you when you ask! the general format to tell the DA is 
###              (entity) (category) (was / is / will be) (item)
###              the general format for asking is what (tense) (entity) (category)?
###              if you want to exit, just type "bye" !
def load_info(dictionary):
    '''
    This is my load_info function It loads the information in 'da.txt'
    and add them into my dictionary
    '''
    info = open('da.txt', 'r')
    for line in info:
        line.strip('\n')
        line_list = line.split(' ')
        rest = line_list[-1]
        index = line_list.index(rest)
        entity = line_list[0:index]
        entity = ' '.join(entity)
        rest = rest.split('|')
        entity = entity+' '+rest[0]+' '+rest[1]
        rest = str(rest[2])
        rest = rest.strip('\n')
        dictionary[entity] = rest
def ask(user_input, dictionary):
    '''
    this is my ask function, if user input is 
    asking, it'll process user input and get the
    key and value in my dictionary
    '''
    '''
    This part of code breaks the user input down to
    entity_category(entity+category), tense and formulates
    the key
    '''
    user_input = user_input.strip('?')
    user_input = user_input.split(' ')
    if 'was' in user_input:
        tense = 'was'
        index = user_input.index('was')
        entity_category = user_input[(index+1):]
    elif 'is' in user_input:
        tense = 'is'
        index = user_input.index('is')
        entity_category = user_input[(index+1):]
    elif 'will' in user_input:
        tense = 'will be'
        index = user_input.index('will')
        entity_category = user_input[(index+2):]
    key = ' '.join(entity_category) + ' ' + tense
    '''
    This part is to reply the user
    the if-elif-else statements are 
    for different conditions
    '''
    if key not in dictionary:
        print("DA: I don't know.")
    elif 'my' in key:
        first_part = key.replace('my', 'your')
        print('DA:', first_part, dictionary[key])
    elif 'your' in key:
        first_part = key.replace('your', 'my')
        print('DA:', first_part, dictionary[key])
    else:
        print('DA:', key, dictionary[key])
def tell(user_input, dictionary):
    '''
    This is my tell function, it will
    breaks the user input down, and 
    re-join them and store them as 
    key and value in the dictionary
    '''
    user_input = user_input.split(' ')
    entity = user_input[0]
    if 'was' in user_input:
        tense = 'was'
        index = user_input.index('was')
        category = user_input[1:index]
        item = user_input[(index+1):]
    elif 'is' in user_input:
        tense = 'is'
        index = user_input.index('is')
        category = user_input[1:index]
        item = user_input[(index+1):]
    elif 'will' in user_input:
        tense = 'will be'
        index = user_input.index('will')
        category = user_input[1:index]
        item = user_input[(index+2):]
    category = ' '.join(category)
    item = ' '.join(item)
    key = entity+' '+category+' '+tense
    dictionary[key] = item
    print('DA: OK!')
def main():
    '''
    This is my main function it creates an
    empty dictionary, and does stop asking 
    for user input unless it is 'bye'
    '''
    dictionary = dict()
    load_info(dictionary)
    print("DA: Hi there, let's talk. . .")
    while True:
        user_input = input('USER:\n')
        if user_input == 'bye':
            print('DA: bye!')
            break
        elif user_input.startswith('what'):
            ask(user_input, dictionary)
        else:
            tell(user_input, dictionary)
main()