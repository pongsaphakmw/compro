import login
import characters,game_1,game_2

def login_menu():
    print('\t\t\tWelcome to Nongbate in wonderland')
    print('\t\tRegister type : 1')
    print('\t\tLogin type : 2')
    while 1:
        choose = int(input('\t\tEnter your choose here : '))
        print('\t----------------------------------------------')
        if choose == 1:
            username = login.Register()
            return username
        elif choose == 2 :
            username = login.Login()
            return username
        else:    
            print('Wrong input!')
            continue
    print('\t----------------------------------------------')
         
def game_menu():
    while 1:
        print('\t\t\tChoose mini games to play')
        print('\t\tGame 1 : Type 1')
        print('\t\tGame 2 : Type 2')
        print('\t\tGame 3 : Type 3')
        print('\t\tScore board : Type "S"')
        print('\t\t\t\t\t\t\t\t\tType "i" to open inventory')
        check = input('Type here : ').lower()
        if check == 'i':
            print('inventory')
            break
        elif check == '1':
            game_1.GAME_1(login_menu())
            check_quit = input('Type "Q" to exit : ').lower()
            if check_quit == 'q':
                break
            else: continue
        elif check == '2':
            game_2.GAME_2(login_menu())
            check_quit = input('Type "Q" to exit : ').lower()
            if check_quit == 'q':
                print('Bye')
                break
            else: continue
        elif check == '3':
            print('game 3')
            break
        elif check == 's':
           print('Score board')
        else:
            print('Wrong input')
            continue
        

# print(main_menu.login_menu())