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
    
    def game_menu():
        print('\t\t\tChoose mini games to play')
        print('\t\tGame 1 : Type 1')
        print('\t\tGame 2 : Type 2')
        print('\t\tGame 3 : Type 3')
        print('\t\t\t\t\t\t\t\t\tType "i" to open inventory')
        

main_menu.game_menu()