### 
### Author: Jasur.Jiasuer
### Description: This is a program that prints out an avatar 
###              Based on your input. You can chose to print 
###              Chris, Jeff and Adam or you can customize!
###              Your input can be either a string or an 
###              Integer for length. Enter The descriptions
###              And get yourself an avatar!
def main():
    '''
    This is my main function, it prints the title of the program
    and it calls avatar_check() function.
    '''
    print('''----- AVATAR -----''')
    avatar_check()
def avatar_check():
    '''
    This function decides wether the input is pre-existing avatars
    or custom avatar or exit.
    avatar: Chris/Jeff/Adam/exit/custom.
    '''
    avatar = input('''Select an Avatar or create your own:\n''')
    if str(avatar) == 'Chris':
        chris()
    elif str(avatar) == 'Jeff':
        jeff()
    elif str(avatar) == 'Adam':
        adam()
    elif str(avatar) == 'exit':
        return
    elif str(avatar) == 'custom':
        custom()
    else:
        avatar_check()
def draw_hat(hat):
    '''
    This function draws the hat you chose!
    '''
    if hat == 'left':
        print('''\n       ~-~       
     /-~-~-\\     
 ___/_______\\    ''')
    elif hat == 'right':
        print('''\n       ~-~       
     /-~-~-\\     
    /_______\\___''')
    elif hat == 'both':
        print('''\n       ~-~       
     /-~-~-\\     
 ___/_______\\___''')
    else:
        print('''\n       ~-~       
     /-~-~-\\     
    /_______\\''')
def draw_hair(hair):
    '''
    This function draws the hair you chose!
    '''
    if hair == 'True':
        print('    |"""""""|')
    elif hair == 'False':
        print("    |'''''''|")
def draw_eye(character):
    '''
    This function draws the eye with the character 
    you chose and it draws the rest of the face.
    '''
    print('    | '+character+'   '+character+' |')
    print('    |   V   |')
    print('    |  ~~~  |')
    print('     \_____/')
def draw_arm(arm):
    '''
    This function draws the arm based on what arm
    style you chose!
    '''
    print(' 0', end='')
    index = 0
    while index < 4:
        print(arm, end='')
        index += 1
    print('|---|', end='')
    while index < 8:
        print(arm, end='')
        index += 1
    print('0')
def draw_torso(torso):
    '''
    This function draws the torso based on the length you chose!
    '''
    while torso > 0:
        print('      |-X-|      ')
        torso -= 1
def draw_leg(leg):
    '''
    This function draws the legs based on the length you chose!
    '''
    print('      HHHHH')
    index = 0
    while leg > 0:
        left_space = 5 - index
        middle_space = 1 + 2*index
        while left_space != 0:
            print(' ', end = '')
            left_space -= 1
        print('///',end = '')
        while middle_space != 0:
            print(' ', end = '')
            middle_space -= 1
        print('\\\\\\')
        leg -= 1
        index += 1
def draw_shoe(shoe):
    '''
    This function draws the shoes based on your input!
    '''
    print(shoe+'       '+shoe)

def jeff():
    '''
    This is a function that draws Jeff!
    '''
    print('''\n       ~-~    
     /-~-~-\     
 ___/_______\___ 
    |"""""""|    
    | 0   0 |    
    |   V   |    
    |  ~~~  |    
     \_____/     
 0====|---|====0
      |-X-|      
      |-X-|      
      HHHHH      
     /// \\\\\\
    ///   \\\\\\
#HHH#       #HHH#''')
         
def adam():
    '''
    This is a function that draws Adam!
    '''
    print("""\n       ~-~       
     /-~-~-\     
    /_______\___ 
    |'''''''|
    | *   * |    
    |   V   |    
    |  ~~~  |    
     \_____/     
      |-X-|      
 0TTTT|---|TTTT0
      |-X-|      
      |-X-|      
      |-X-|      
      HHHHH      
     /// \\\\\\
    ///   \\\\\\
   ///     \\\\\\
<|||>       <|||>""")
def chris():
    '''
    This is a function that draws Chris!
    '''
    print('''\n       ~-~       
     /-~-~-\     
    /_______\    
    |"""""""|    
    | U   U |    
    |   V   |    
    |  ~~~  |    
     \_____/     
      |-X-|      
 0WWWW|---|WWWW0
      |-X-|      
      HHHHH      
     /// \\\\\\
    ///   \\\\\\
   ///     \\\\\\
  ///       \\\\\\
<>-<>       <>-<>''')
def custom():
    '''
    This function takes all the input and pass them to specific functions.
    hat: left/right/both.
    character: a string or a number.
    hair: True/False
    torso: a popsitive integer.
    leg: a positive integer between 1 - 4.
    shoe: 5 characters long, can be strings or numbers.
    '''
    print('Answer the following questions to create a custom avatar')
    hat = str(input('Hat style ?\n'))
    character = input('Character for eyes ?\n')
    hair = str(input('Shaggy hair (True/False) ?\n'))
    arm = input('Arm style ?\n')
    torso = int(input('Torso length ?\n'))
    leg = int(input('Leg length (1-4) ?\n'))
    shoe = input('Shoe look ?\n')
    draw_hat(hat)
    draw_hair(hair)
    draw_eye(character)
    draw_arm(arm)
    draw_torso(torso)
    draw_leg(leg)
    draw_shoe(shoe)
main()