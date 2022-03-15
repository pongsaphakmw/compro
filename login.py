import re
import hashlib
'''
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
Check e-mail
'''
username,email,password,password2 = None,None,None,None #debugger
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
                # user_data = [email,username,hash1]
                with open('user1.txt','w') as f:
                    # f.write(str(user_data)+'\n')
                    f.write('%s,%s,%s'%(email,username,hash1))
                    f.close()
                return username,email,password,password2,hash1
            else:
                print('Wrong E-mail!')
                continue
        else:
            print('Wrong password!')
            continue

def Login():
    
    while 1:
        login_user = input('Enter username or email : ')
        login_pass = input('Enter pass word : ')
        auth = login_pass.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        with open('user1.txt','r') as f:
            stored_email,stored_user,stored_pass = f.read().split(',')
        f.close()
        print(stored_email)
        print(auth_hash)
        print(stored_pass)
        if login_user == stored_email or login_user == stored_user:
            if auth_hash == stored_pass:
                print('Login success!')
                return True
            else:
                print('Wrong password!')
                continue
        else:
            print('Wrong username!')
            continue
    
# Register() #debugger
Login()
