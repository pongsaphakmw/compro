import json
import login
import characters,game_1,game_2,game_3

def login_menu():
    print('''

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

░██╗░░░░░░░██╗░█████╗░███╗░░██╗██████╗░███████╗██████╗░██╗░░░░░░█████╗░███╗░░██╗██████╗░
░██║░░██╗░░██║██╔══██╗████╗░██║██╔══██╗██╔════╝██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔══██╗
░╚██╗████╗██╔╝██║░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝██║░░░░░███████║██╔██╗██║██║░░██║
░░████╔═████║░██║░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗██║░░░░░██╔══██║██║╚████║██║░░██║
░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║██████╔╝███████╗██║░░██║███████╗██║░░██║██║░╚███║██████╔╝
░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░
''')
    print('\t────────────────────────────────────────────────────────────────')
    print('\t\tRegister type : 1')
    print('\t\tLogin type : 2')
    while 1:
        choose = input('\t\tEnter your choose here : ')
        choose = int(choose)
        print('\t────────────────────────────────────────────────────────────────')
        if choose == 1:
            username = login.Register()
            return username
        elif choose == 2 :
            username = login.Login()
            return username
        else:    
            print('Wrong input!')
            continue
    print('\t────────────────────────────────────────────────────────────────')

def score_board(user_score):
    with open('score.json','r') as sb:
        sb_data = json.load(sb)
        print('\t────────────────────────────────────────────────────────────────')
        print('\t\tScore board!!')
        for i in range(len(sb_data)):
            print(sb_data[i]['user'],'\t\t\t\t',sb_data[i]['score'])
        print('\t────────────────────────────────────────────────────────────────')
         
def game_menu():
    username = login_menu()
    while 1:
        print('\t\t\tChoose mini games to play')
        print('\t\tGame 1 : Type 1')
        print('\t\tGame 2 : Type 2')
        print('\t\tGame 3 : Type 3')
        print('\t\tScore board : Type "S"')
        print('\t\t\t\t\t\t\t\t\tType "i" to open inventory')
        check = input('Type here : ').lower()
        if check == 'i':
            characters.Character.Inventory(username)
            
        elif check == '1':
            game_1.GAME_1(username)
            check_quit = input('Type "Q" to exit : ').lower()
            print('\t────────────────────────────────────────────────────────────────')
            if check_quit == 'q':
                print('''
                
██████╗░██╗░░░██╗███████╗  ██╗
██╔══██╗╚██╗░██╔╝██╔════╝  ██║
██████╦╝░╚████╔╝░█████╗░░  ██║
██╔══██╗░░╚██╔╝░░██╔══╝░░  ╚═╝
██████╦╝░░░██║░░░███████╗  ██╗
╚═════╝░░░░╚═╝░░░╚══════╝  ╚═╝
                ''')
                break
            else: continue
        elif check == '2':
            game_2.GAME_2(username)
            check_quit = input('Type "Q" to exit : ').lower()
            if check_quit == 'q':
                print('''
                
██████╗░██╗░░░██╗███████╗  ██╗
██╔══██╗╚██╗░██╔╝██╔════╝  ██║
██████╦╝░╚████╔╝░█████╗░░  ██║
██╔══██╗░░╚██╔╝░░██╔══╝░░  ╚═╝
██████╦╝░░░██║░░░███████╗  ██╗
╚═════╝░░░░╚═╝░░░╚══════╝  ╚═╝
                ''')
                break
            else: continue
        elif check == '3':
            game_3.GAME_3(username)
            check_quit = input('Type "Q" to exit : ').lower()
            if check_quit == 'q':
                print('''
                
██████╗░██╗░░░██╗███████╗  ██╗
██╔══██╗╚██╗░██╔╝██╔════╝  ██║
██████╦╝░╚████╔╝░█████╗░░  ██║
██╔══██╗░░╚██╔╝░░██╔══╝░░  ╚═╝
██████╦╝░░░██║░░░███████╗  ██╗
╚═════╝░░░░╚═╝░░░╚══════╝  ╚═╝
                ''')
                break
        elif check == 's':
           score_board(username)
        else:
            print('Wrong input')
            continue
        

# print(main_menu.login_menu())