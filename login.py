import re
import hashlib
import json
from textwrap import indent
'''
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
Check e-mail
'''
'''
**************** Important Note! ****************
Don't change anything if u don't know how to use stackoverflow XD
'''

def Register():
    with open('user1.json','r') as f:
        data = json.load(f)
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        while 1:
            email = input('Enter your email here : ')
            username = input('Enter your username here : ')
            password = input('Enter your pass word : ')
            password2 = input('Confirm your pass word : ')
            
                
            if password2 == password:
                if (re.fullmatch(regex, email)):
                    enc = password2.encode()
                    hash1 = hashlib.md5(enc).hexdigest()
                    
                    for i in range(len(data)):
                        if data[i]['mail'] == email or data[i]['user'] == username:
                            print('email or user name is unaviable try again!')
                            Register()
                            user_data = {'mail':email,'user':username,'pass':hash1}
                    else:
                        user_data = {'mail':email,'user':username,'pass':hash1}
                        data.append(user_data)
                        with open('user1.json','w') as f:
                            json.dump(data, f, indent=4)
                        return user_data
                else:
                    print('Wrong E-mail!')
                    continue
            else:
                print('Wrong password!')
                continue    

def Login():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while 1:
        login_user = input('Enter username or email : ')
        login_pass = input('Enter pass word : ')
        auth = login_pass.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        with open('user1.json','r') as f:
            x = 0;y = 0;z=0
            dict = json.loads(f.read())
            while x <= len(dict):
                if y >= len(dict):
                    print('Wrong pass word')
                    break
                elif x >= len(dict):
                    print('Wrong username!')
                    break
                elif z >= len(dict):
                    print('Wrong username!')
                    break
                check_user = dict[x]['user']
                check_mail = dict[x]['mail']
                check_pass = dict[x]['pass']
                # print(check_pass)
                if login_user == check_user or login_user == check_mail :
                    if auth_hash == check_pass:
                        print('Login success!')
                        print('Welcome %s !'%check_user)
                        return check_user
                    else:
                        y+=1
                else:
                    x+=1
                    if login_user in regex:
                        z+=1
            else:
                continue
     
 
# Register() #debugger
# Login()
# print(Login())
# with open('user1.json','r') as f:
#     list_user = json.loads(f.read())    
