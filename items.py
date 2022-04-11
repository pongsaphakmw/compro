import characters

class items_damage:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class items_defend:
    def __init__(self, name, armor):
        self.name = name
        self.armor = armor

def game_items():
    items = [
        {'Wooden_sword' : items_damage('Wooden_sword',5)},
        {'Iron_sword' : items_damage('Iron_sword',10)},
        {'Diamond_sword' : items_damage('Diamond_sword',15)},
        {'Platinum_sword' : items_damage('Platinum_sword',20)},
        {'Leather_armor' : items_defend('Leather_armor',3)},
        {'Chain_armor' : items_defend('Chain_armor',5)},
        {'Iron_armor' : items_defend('Iron_armor',7)},
        {'Paladin_armor' : items_defend('Paladin_armor',15)},
        {'God_armor' : items_defend('God_armor',50)}
    ]
