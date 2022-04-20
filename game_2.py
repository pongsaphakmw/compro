import json
import characters
from random import randint
def GAME_2(user_name):
    player = characters.Game_items.game_list()

    print("Game 2 ....")
    state = int(input("choose state : "))
    if state == 1:
        print("Welcome to State 1")
        print("Calculate the equation to get rid of monsters!!")
        print("------------------------------")
        MaxHP_main = player[0][0]['main_char'].HP
        MaxHP_monster = player[0][1]['monster'].HP
        while 1:
            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
            print("%s  have HP %s "%(player[0][1]['monster'].name,player[0][1]['monster'].HP))
            print("------------------------------")
            if player[0][0]['main_char'].HP<=0:
                print("\tlose")
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][1]['monster'].reset(MaxHP_monster)
                break
            # Next patch XD!
            elif player[0][0]['main_char'].HP <=50:
                print('Need healing?')
                print('Open your inventory to heal')
                inv = input('Type "I" to open inventory : ').lower()
                if inv == 'i':
                    char_inv = characters.Character.Inventory(user_name)
                    choose = input('Choose your potion by number : ')
                    choose = int(choose)
                    for i in range(len(char_inv)):
                        if choose == i:
                            player[0][0]['main_char'].use_potion(char_inv[i]['item'],1,user_name)
                            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
                            # แก้บัคได้แล้วกุแม่งเก่งว่ะ
            elif player[0][1]['monster'].HP<=0:
                print("\twon")
                x = randint(0,4);y = randint(0,2)
                characters.collect_items(user_name,x,y)
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][1]['monster'].reset(MaxHP_monster)
                with open('score.json','r') as sc:
                    score_data = 0
                    sc_data = json.load(sc)
                    
                    for i in range(len(sc_data)):
                        if sc_data[i]['user'] == user_name:
                            sc_data[i]['score'] += 10
                            break
                    else:
                        score_data += 10
                        score = {'user': user_name,'score':score_data}
                        sc_data.append(score)
                with open('score.json','w') as sc:
                    json.dump(sc_data,sc,indent=4)
                break

            for i in range(1):
                x = randint(1,90)
                y = randint(1,90)
                randomproblem = x+y
                print("%d + %d"%(x, y))
                #print(randomproblem)
                answer = int(input("In put your answer: "))
                print("------------------------------")
                if answer == randomproblem:
                    print("\tCorrect!!!")
                    print("------------------------------")
                    player[0][1]['monster'].name,player[0][1]['monster'].Attack(10)
                    print("\tyou have done damage!!!")
                    print("------------------------------")
                    break
                elif answer != randomproblem:
                    print("\tTry again!!!")
                    print("------------------------------")
                    player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)
                    print("\tGot damage!!!")
                    print("------------------------------")
                    break
    elif state == 2:
        print("Welcome to State 2")
        print("Calculate the equation to get rid of monsters!!")
        print("------------------------------")
        MaxHP_main = player[0][0]['main_char'].HP
        MaxHP_monster = player[0][2]['monster'].HP
        while 1:
            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
            print("%s  have HP %s "%(player[0][2]['monster'].name,player[0][2]['monster'].HP))
            print("------------------------------")
            if player[0][0]['main_char'].HP<=0:
                print("\tlose")
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][2]['monster'].reset(MaxHP_monster)
                break
            elif player[0][2]['monster'].HP<=0:
                print("\twon")
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][2]['monster'].reset(MaxHP_monster)
                with open('score.json','r') as sc:
                    score_data = 0
                    sc_data = json.load(sc)
                    
                    for i in range(len(sc_data)):
                        if sc_data[i]['user'] == user_name:
                            sc_data[i]['score'] += 10
                            break
                    else:
                        score_data += 10
                        score = {'user': user_name,'score':score_data}
                        sc_data.append(score)
                with open('score.json','w') as sc:
                    json.dump(sc_data,sc,indent=4)
                break

            for i in range(1):
                x = randint(1,90)
                y = randint(1,90)
                randomproblem = x-y
                print("%d - %d"%(x, y))
                #print(randomproblem)
                answer = int(input("In put your answer: "))
                print("------------------------------")
                if answer == randomproblem:
                    print("\tCorrect!!!")
                    print("------------------------------")
                    player[0][2]['monster'].name,player[0][2]['monster'].Attack(10)
                    print("\tyou have done damage!!!")
                    print("------------------------------")
                    break
                elif answer != randomproblem:
                    print("\tTry again!!!")
                    print("------------------------------")
                    player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)
                    print("\tGot damage!!!")
                    print("------------------------------")
                    break
    elif state == 3:
        print("Welcome to State 3")
        print("Calculate the equation to get rid of monsters!!")
        print("------------------------------")
        MaxHP_main = player[0][0]['main_char'].HP
        MaxHP_monster = player[0][3]['monster'].HP
        while 1:
            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
            print("%s  have HP %s "%(player[0][4]['monster'].name,player[0][4]['monster'].HP))
            print("------------------------------")
            if player[0][0]['main_char'].HP<=0:
                print("\tlose")
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][3]['monster'].reset(MaxHP_monster)
                break
            elif player[0][4]['monster'].HP<=0:
                print("\twon")
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][3]['monster'].reset(MaxHP_monster)
                with open('score.json','r') as sc:
                    score_data = 0
                    sc_data = json.load(sc)
                    
                    for i in range(len(sc_data)):
                        if sc_data[i]['user'] == user_name:
                            sc_data[i]['score'] += 10
                            break
                    else:
                        score_data += 10
                        score = {'user': user_name,'score':score_data}
                        sc_data.append(score)
                with open('score.json','w') as sc:
                    json.dump(sc_data,sc,indent=4)
                break

            for i in range(1):
                x = randint(1,90)
                y = randint(1,90)
                randomproblem = x*y
                print("%d * %d"%(x, y))
                #print(randomproblem)
                answer = int(input("In put your answer: "))
                print("------------------------------")
                if answer == randomproblem:
                    print("\tCorrect!!!")
                    print("------------------------------")
                    player[0][4]['monster'].name,player[0][4]['monster'].Attack(10)
                    print("\tyou have done damage!!!")
                    print("------------------------------")
                    break
                elif answer != randomproblem:
                    print("\tTry again!!!")
                    print("------------------------------")
                    player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)
                    print("\tGot damage!!!")
                    print("------------------------------")
                    break
