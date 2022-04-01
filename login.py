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
Don't change anything
'''
db_user = []
def Register():
    
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
                user_data = {'mail':email,'user':username,'pass':hash1}
                db_user.append(user_data)
                
                with open('user1.json','r') as f:
                    data = json.load(f)
                
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
                check_mail = dict[z]['mail']
                check_pass = dict[y]['pass']
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
                    # if x <= len(dict):
                    #     continue
                    # else:
                    #     break
            else:
                continue
     
 
# Register() #debugger
# Login()
# print(Login())
# with open('user1.json','r') as f:
#     list_user = json.loads(f.read())    
