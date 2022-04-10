from menu import main_menu
import characters, login

if __name__ == '__main__':
    print('Welcome to our game')
    main_menu.login_menu()
    All_char = characters.Game_items.game_list()
    print("%s : Welcome to Wonderland "%(All_char[0][3]['monster'].stamina)) # Use this format only cuz im lazy to  change
    # main_menu.game_menu()
    # characters.game_timer(10)
    characters.Character.collect_items(login.Login,All_char[1][3]['potion'].name,All_char[1][3]['potion'].space)

    