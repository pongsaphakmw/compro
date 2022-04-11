from menu import main_menu
import characters, login

if __name__ == '__main__':
    print('Welcome to our game')
    main_menu.login_menu()
    All_char = characters.Game_items.game_list()
    print("%s : Welcome to Wonderland "%(All_char[0][0]['main_char'].name)) # Use this format only cuz im lazy to  change
    # main_menu.game_menu()
    characters.collect_items(login.Login(),1,1)
    