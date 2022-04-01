import login

class main_menu:
    def login_menu():
        print('\t\t\tWelcome to Nongbate in wonderland')
        print('\t\tRegister type : 1')
        print('\t\tLogin type : 2')
        while 1:
            choose = int(input('\t\tEnter your choose here : '))
            print('\t----------------------------------------------')
            if choose == 1:
                login.Register()
                break
            elif choose == 2 :
                login.Login()
                break
            else:    
                print('Wrong input!')
                continue
        print('\t----------------------------------------------')
         
    def game_menu():
        print('\t\t\tChoose mini games to play')
        print('\t\tGame 1 : Type 1')
        print('\t\tGame 2 : Type 2')
        print('\t\tGame 3 : Type 3')
        print('\t\t\t\t\t\t\t\t\tType "i" to open inventory')
        while 1:
            check = input('Type here : ')
            if check == 'i':
                print('inventory')
                break
            elif check == '1':
                print('game 1')
                break
            elif check == '2':
                print('game 2')
                break
            elif check == '3':
                print('game 3')
                break
            else:
                print('Wrong input')
                continue
        

# main_menu.game_menu()