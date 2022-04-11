import json
import time
class Character:
    def __init__(self, name, HP, stamina, Slots, sheilds):
        self.name = name
        self.HP = HP
        self.stamina = stamina
        self.Slots = Slots
        self.sheilds = sheilds

    def Heal(self, heal):
        self.HP = self.HP + heal
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

    # def collect_items(user_char,item,qty):
    #     collecting = {'user' : user_char, 'item' : item, 'quantities' : qty}
    #     # with open('inventory.json','r') as cl:
    #     #     inv_data = json.load(cl)

    #     # inv_data.append(collecting)

    #     with open('inventory.json','w') as cl:
    #         json.dumps(collecting.__dict__)

# for database object calculate only NOT! for game
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
        # Edit game items here use class Game_items(ชื่อของ, จำนวน, ใช้พื้นที่เท่าไหร่)
        # เสร็จแล้วก็เก็บไว้เป็น dict ใน list(all_items)
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
            {'armor' : Game_items('Leather_armor',1,1)},
            {'armor' : Game_items('Chain_armor',1,1)},
            {'armor' : Game_items('Iron_armor',1,1)},
            {'armor' : Game_items('Paladin_armor',1,2)},
            {'armor' : Game_items('God_armor',1,4)}
        ]
        # print(all_char[2]['monster'].name) #debugger
        return all_char, all_items

def collect_items(user_char,n,qty):
    potion_item_name = Game_items.game_list()[1][n]['potion'].name
    potion_item_qty = (Game_items.game_list()[1][n]['potion'].space)*qty
    change_form = {'user' : user_char,'item' : potion_item_name, 'qty' : potion_item_qty}
    with open('inventory.json','w') as cl:
        json.dump(change_form,cl,indent=4)
    return user_char,potion_item_name,qty

print(Game_items.game_list()[0][1]['monster'].__dict__)



# game_timer(10)
# Game_items.game_list()