import re
import json

def Register():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while 1:
        user = input('Enter your email here : ')
        if (re.fullmatch(regex, user)):
            password = input('Enter your password here : ')
            con_password = input('Confirm your password : ')
            if password == con_password:
                user_data = {'mail':user, 'pass': con_password}
                with open('user2.json','r') as d:
                    data = json.load(d)

                data.append(user_data)

                with open('user2.json','w') as d:
                    json.dump(data, d, indent=4)
                return user_data # ไม่ใส่ก็ได้
        else:
            print('Wrong email try again!')
            continue
        
def Login():
    while 1:
        login_user = input('ใส่เข้าน้องมาเลยน้องจ๋า : ')
        login_pass = input('ใส่มาเลยพี่จ๋า : ')
        with open('user2.json','r') as d:
            a = 0;b = 0
            mydict = json.loads(d.read())
            while a <= len(mydict):
                if b >= len(mydict):
                    print('Wrong pass word จ่ะพี่จ๋า')
                    break
                elif a >= len(mydict):
                    print('Wrong username จ่ะพี่จ๋า')
                    break
                check_user = mydict[a]['mail']
                check_pass = mydict[a]['pass']
                if login_user == check_user:
                    if login_pass == mydict[a]['pass']:
                        print('login success!')
                        return check_user
                    else:
                        b += 1       
                else:
                    a +=1
            else:
                continue
    
# Register()
Login()