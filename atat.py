### 
### Author: Jasur.Jiasuer
### Description:    This is a that program prints out AT-AT.
###                 Enter the Neck Length, Body Height,
###                 Leg Height to get the AT-AT you like!
neck_length = int(input('Neck Length:\n'))
body_height = int(input('Body Height:\n'))
leg_height = int(input('Leg Height:\n'))
print('''\n     _,.-Y  |  |  Y-._
 .-~"   ||  |  |  |   "-.''')
print(' |______________________|\n'*body_height,end='')
print(' |______________________| '+' '*neck_length+'   _____')
print(''' L______________________[--'''+'-'*neck_length+'''-I" .-{"-.''')
print('I____________________ [__L]'+'_'*neck_length+'[I_/r(=}=-P')
print('''L________________________j~'''+' '*neck_length+''' '-=c_]/=-^''')
print('\________________________]')
print('  [___________________]')
print('''     I--I"~~"""~~"I--I''')
print('     |\\n|         |\\n|\n'*leg_height,end='')
print('''     ([])         ([])
    /|..|\       /|..|\\
   |=}--{=|     |=}--{=|
  .-^--e-^-.   .-^--e-^-.''')