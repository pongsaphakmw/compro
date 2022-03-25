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

