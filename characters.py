import json
import time
class Character:
    def __init__(self, name, HP, stamina, Slots, sheilds):
        self.name = name
        self.HP = HP
        self.stamina = stamina
        self.Slots = Slots
        self.sheilds = sheilds

    def Health(self, start_health):
        self.HP = self.HP + start_health
    def Inventory(self,inv_slots): # Inprogress it's hard ;-;
        with open('inventory.json','r') as inv:
            data_inv = json.load(inv)

        self.Slots = self.Slots - inv_slots

        data_inv.append(self.Slots)

        with open('inventory.json','w') as inv:
            json.dump(data_inv,inv,indent=4)

        return self(inv_slots)
    def Stamina(self,start_stamina):
        self.stamina = self.stamina + start_stamina
    def Sheild(self, add_sheild):
        self.sheilds = self.sheilds + add_sheild
    def Attack(self, attack_damage):
        self.HP = self.HP - attack_damage

    def collect_items(user_char,item,qty):
        collecting = {'user' : user_char, 'item' : item, 'quantities' : qty}
        with open('inventory.json','r') as cl:
            inv_data = json.load(cl)

        inv_data.append(collecting)

        with open('inventory.json','w') as cl:
            json.dump(inv_data,cl,indent=4)

class Game_items:
    def __init__(self, name, qty, space):
        self.name = name
        self.qty = qty
        self.space = space

    def __repr__(self) -> str:
        self(all_char = [])

    def Inventory_space(self, inv_slots):
        self.space = self.space - inv_slots


    def game_list():
        # You can add characters here. I think stored in DB would be better
        all_char = [
        {'main_char' : Character('Nongbate', 100, 50, 4, 3)},
        {'monster' : Character('คิดชื่อเอา', 30, 15, 0, 0)},
        {'monster' : Character('คิดชื่อเอา2', 50, 30, 0, 0)},
        {'monster' : Character('คิดเอา3', 30, 30, 0, 0)},
        {'monster' : Character('คิดเอา4', 30, 30, 0, 0)}
        ]

        all_items = [
            {'potion' : Game_items('Blue_potion', 1, 1)},
            {'potion' : Game_items('Yellow_potion',1,1)},
            {'potion' : Game_items('Red_potion',1,1)},
            {'potion' : Game_items('White_potion',1,1)},
            {'potion' : Game_items('????',1,1)},
            {'sword' : Game_items('Wooden_sword',1,1)},
            {'sword' : Game_items('Iron_sword',1,1)},
            {'sword' : Game_items('Diamond_sword',1,1)},
            {'sword' : Game_items('Platinum_sword',1,1)},
            {'armor' : Game_items('Leather_armor',1,1)}
        ]
        # print(all_char[0]['main_char'].Slots) #debugger
        return all_char, all_items


def game_timer(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("time out!")

# game_timer(10)
# char_list()