from menu import main_menu
import characters, login

if __name__ == '__main__':
    print('Welcome to our game')
    user = main_menu.login_menu()
    All_char = characters.Game_items.game_list()
    print("%s : Welcome to Wonderland "%(All_char[0][0]['main_char'].name)) # Use this format only cuz im lazy to  change
    # main_menu.game_menu()
    # ช่องแรกคือ user ช่อง2คือตำแหน่งไอเทมในลิสดูในไฟล์ characters ช่อง3คือจำนวน
    characters.collect_items(user,2,1)
    # แก้บัคเพิ่มของหมวดอื่นไม่ได้