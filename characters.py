import time,json
class Character:
    def __init__(self, name, HP, stamina, Slots, sheilds):
        self.name = name
        self.HP = HP
        self.stamina = stamina
        self.Slots = Slots
        self.sheilds = sheilds
        self.reset(HP)

    def reset(self,HP):
        self.HP = HP

    def Heal(self, heal):
        self.HP = self.HP + heal
    def Inventory(user_check):
        print('You have : ')
        vir_inv = []
        with open('inventory.json','r') as inv:
            data_inv = json.load(inv)
            for i in range(len(data_inv)):
                if data_inv[i]['user'] == user_check:
                    print('\t',data_inv[i]['item'],data_inv[i]['qty'])
                    vir_inv.append(data_inv[i])
            return vir_inv

    def Stamina(self,start_stamina):
        self.stamina = self.stamina + start_stamina
    def Sheild(self, add_sheild):
        self.sheilds = self.sheilds + add_sheild
    def Attack(self, attack_damage):
        self.HP = self.HP - attack_damage
    def use_potion(self,potion_name,qty,user_name):
        MaxHP = Game_items.game_list()[0][0]['main_char'].HP
        with open('inventory.json','r') as uspo:
            uspo_data = json.load(uspo)
            for i in range(len(uspo_data)):
                if uspo_data[i]['user'] == user_name:
                    if uspo_data[i]['item'] == potion_name:
                        # uspo_data[i]['qty'] = uspo_data[i]['qty'] - qty
                        if potion_name == 'Blue_potion':
                            self.Heal(10)
                            uspo_data[i]['qty'] = uspo_data[i]['qty'] - qty
                            break
                        elif potion_name == 'Yellow_potion':
                            self.Heal(20)
                            uspo_data[i]['qty'] = uspo_data[i]['qty'] - qty
                            break
                        elif potion_name == 'Red_potion':
                            self.Heal(30)
                            uspo_data[i]['qty'] = uspo_data[i]['qty'] - qty
                            break
                        elif potion_name == 'White_potion':
                            self.Heal(40)
                            uspo_data[i]['qty'] = uspo_data[i]['qty'] - qty
                            break
                        elif potion_name == '????':
                            self.reset(MaxHP)
                            uspo_data[i]['qty'] = uspo_data[i]['qty'] - qty
                            break
                        else:
                            print("you don't have that item !")
        
        with open('inventory.json','w') as uspo:
            json.dump(uspo_data,uspo,indent=4)

# for database obiect calculate only NOT! for game
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
        {'monster' : Character('Soju', 30, 15, 0, 0)},
        {'monster' : Character('Sang Som', 40, 30, 0, 0)},
        {'monster' : Character('Kaw Noy', 50, 30, 0, 0)},
        {'monster' : Character('Raw Pok', 60, 30, 0, 0)}
        ]
        # Edit game items here use class Game_items(?????????????????????, ???????????????, ??????????????????????????????????????????????????????)
        # ?????????????????????????????????????????????????????????????????? dict ?????? list(all_items)
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
            {'armour' : Game_items('Leather_armour',1,1)},
            {'armour' : Game_items('Chain_armour',1,1)},
            {'armour' : Game_items('Iron_armour',1,1)},
            {'armour' : Game_items('Paladin_armour',1,2)},
            {'armour' : Game_items('God_armour',1,4)}
        ]
        # print(all_char[2]['monster'].name) #debugger
        return all_char, all_items
# Next patch XD!
def collect_items(user_char,n,qty):
    
    with open('inventory.json','r') as cl:
        data = json.load(cl)
        for i in range(len(data)):
            if n >= 0 and n <= 4:
                potion_item_name = Game_items.game_list()[1][n]['potion'].name
                potion_item_qty = (Game_items.game_list()[1][n]['potion'].space)*qty
                change_form_potion = {'user' : user_char,'item' : potion_item_name, 'qty' : potion_item_qty}
                
                if data[i]["qty"] != 0 and data[i]['item'] == potion_item_name and data[i]['user'] == user_char:
                    data[i]['qty'] += potion_item_qty
                    break
            elif n <= 8:
                sword_item_name = Game_items.game_list()[1][n]['sword'].name
                sword_item_qty = (Game_items.game_list()[1][n]['sword'].space)*qty
                change_form_sword = {'user' : user_char,'item' : sword_item_name, 'qty' : sword_item_qty}
                if data[i]["qty"] != 0 and data[i]['item'] == sword_item_name and data[i]['user'] == user_char:
                    data[i]['qty'] += sword_item_qty
                    break
            elif n <= 13:
                armour_item_name = Game_items.game_list()[1][n]['armour'].space
                armour_item_qty = (Game_items.game_list()[1][n]['armour'].space)*qty
                change_form_armour = {'user' : user_char,'item' : armour_item_name, 'qty' : armour_item_qty}
                if data[i]["qty"] != 0 and data[i]['item'] == armour_item_name and data[i]['user'] == user_char:
                    data[i]['qty'] += armour_item_qty
                    break 
        else:
            for j in range(len(data)):
                if n >=0 and n <=4:
                    if data[j]['item'] != potion_item_name: 
                        data.append(change_form_potion)
                        break
                elif n <= 8:
                    print(data[j]['item'])
                    if data[j]['item'] != sword_item_name:
                        data.append(change_form_sword)
                        break
                elif n <= 13:
                    if data[j]['item'] != armour_item_name:
                        data.append(change_form_armour)
                        break

    with open('inventory.json','w') as cl:
        json.dump(data,cl,indent=4)
    
    return user_char,qty
# Next patch XD!

                


# print(Game_items.game_list()[0][1]['monster'].__dict__)



# game_timer(10)
# Game_items.game_list()