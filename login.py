import re
'''
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
Check e-mail
'''
username,email,password,password2 = None,None,None,None #debugger
def Register(username,email,password,password2):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while 1:
        email = input('Enter your email here : ')
        username = input('Enter your username here : ')
        password = input('Enter your pass word : ')
        password2 = input('Confirm your pass word : ')
        if password2 == password:
            if (re.fullmatch(regex, email)):
                f = open('user1.txt', 'w')
                f.write('E-mail : %s, User : %s, Pass : %s'%(email,username,password))
                return username,email,password,password2
            else:
                print('Wrong E-mail!')
                continue
        else:
            print('Wrong password!')
            continue

def Login():
    pass

Register(username,email,password,password2) #debugger