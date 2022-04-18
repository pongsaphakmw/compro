import json
import characters
from random import randint
player = characters.Game_items.game_list()
def GAME_1(user_name):
    print("Game 1 ....") 
    state = int(input("choose state :"))
    if state == 1:  
        print("Welcome to State 1")
        print("Attack  = 1")
        print("Counter = 2")
        print("Magic   = 3")
        MaxHP_main = player[0][0]['main_char'].HP
        MaxHP_monster = player[0][1]['monster'].HP
        while 1:
            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
            print("%s  have HP %s "%(player[0][1]['monster'].name,player[0][1]['monster'].HP))     
            if player[0][0]['main_char'].HP<=0:
                print("lose")
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][1]['monster'].reset(MaxHP_monster)
                break
            elif player[0][1]['monster'].HP<=0:
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][1]['monster'].reset(MaxHP_monster)
                print("won")
                
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
            Useskill=int(input("Use skill : "))
            print("Monster Use ")
        
            for i in range(1): 
                r = randint(1,3)
                if r == 1:
                    print("Attack")    
                elif r == 2 :
                    print ("Counter")
                elif r == 3 :
                    print ("Magic")
            if Useskill == 1 and r == 1:
                player[0][1]['monster'].name,player[0][1]['monster'].Attack(0)
                print("Draw")
            elif Useskill == 1 and r == 2:
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)
                print("Got damage")
            elif Useskill == 1 and r == 3:
                player[0][1]['monster'].name,player[0][1]['monster'].Attack(10)
                print("you have done damage")           
            elif Useskill == 2 and r == 1:
                
                player[0][1]['monster'].name,player[0][1]['monster'].Attack(10)
                print("you have done damage")
            elif Useskill == 2 and r == 2:
                player[0][1]['monster'].name,player[0][1]['monster'].Attack(0)
                
                print("Draw")
            elif Useskill == 2 and r == 3:
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)         
                print("Got damage")
            elif Useskill == 3 and r == 1:                  
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)
                print("Got damage")
            elif Useskill == 3 and r == 2:      
                player[0][1]['monster'].name,player[0][1]['monster'].Attack(10)   
                print("you have done damage")         
            elif Useskill == 3 and r == 3:
                player[0][1]['monster'].name,player[0][1]['monster'].Attack(0)
                print("Draw")
            elif Useskill >=4:
                break
    elif state == 2:  
        print("Welcome to State 2")
        print("Attack  = 1")
        print("Counter = 2")
        print("Magic   = 3")
        MaxHP_main = player[0][0]['main_char'].HP
        MaxHP_monster = player[0][2]['monster'].HP
        while 1:
            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
            print("%s  have HP %s "%(player[0][2]['monster'].name,player[0][2]['monster'].HP))     
            if player[0][0]['main_char'].HP<=0:
                print("lose")
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][2]['monster'].reset(MaxHP_monster)
                break
            elif player[0][2]['monster'].HP<=0:
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][2]['monster'].reset(MaxHP_monster)
                print("won")

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
                
            Useskill=int(input("Use skill : "))
            print("Monster Use ")
        
            for i in range(1): 
                r = randint(1,3)
                if r == 1:
                    print("Attack")    
                elif r == 2 :
                    print ("Counter")
                elif r == 3 :
                    print ("Magic")
            if Useskill == 1 and r == 1:
                player[0][2]['monster'].name,player[0][2]['monster'].Attack(0)
                print("Draw")
            elif Useskill == 1 and r == 2:
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)
                print("Got damage")
            elif Useskill == 1 and r == 3:
                player[0][2]['monster'].name,player[0][2]['monster'].Attack(10)
                print("you have done damage")           
            elif Useskill == 2 and r == 1:
                
                player[0][2]['monster'].name,player[0][2]['monster'].Attack(10)
                print("you have done damage")
            elif Useskill == 2 and r == 2:
                player[0][2]['monster'].name,player[0][2]['monster'].Attack(0)
                
                print("Draw")
            elif Useskill == 2 and r == 3:
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)         
                print("Got damage")
            elif Useskill == 3 and r == 1:                  
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)
                print("Got damage")
            elif Useskill == 3 and r == 2:      
                player[0][2]['monster'].name,player[0][2]['monster'].Attack(10)   
                print("you have done damage")         
            elif Useskill == 3 and r == 3:
                player[0][2]['monster'].name,player[0][2]['monster'].Attack(0)
                print("Draw")
            elif Useskill >=4:
                break
    elif state == 3:  
        print("Welcome to State 3")
        print("Attack  = 1")
        print("Counter = 2")
        print("Magic   = 3")
        MaxHP_main = player[0][0]['main_char'].HP
        MaxHP_monster = player[0][3]['monster'].HP
        while 1:
            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
            print("%s  have HP %s "%(player[0][3]['monster'].name,player[0][3]['monster'].HP))     
            if player[0][0]['main_char'].HP<=0:
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][3]['monster'].reset(MaxHP_monster)
                print("lose")
                break
            elif player[0][3]['monster'].HP<=0:
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][3]['monster'].reset(MaxHP_monster)
                print("won")
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
            Useskill=int(input("Use skill : "))
            print("Monster Use ")
        
            for i in range(1): 
                r = randint(1,3)
                if r == 1:
                    print("Attack")    
                elif r == 2 :
                    print ("Counter")
                elif r == 3 :
                    print ("Magic")
            if Useskill == 1 and r == 1:
                player[0][3]['monster'].name,player[0][3]['monster'].Attack(0)
                print("Draw")
            elif Useskill == 1 and r == 2:
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(12)
                print("Got damage")
            elif Useskill == 1 and r == 3:
                player[0][3]['monster'].name,player[0][3]['monster'].Attack(10)
                print("you have done damage")           
            elif Useskill == 2 and r == 1:
                
                player[0][3]['monster'].name,player[0][3]['monster'].Attack(10)
                print("you have done damage")
            elif Useskill == 2 and r == 2:
                player[0][3]['monster'].name,player[0][3]['monster'].Attack(0)
                
                print("Draw")
            elif Useskill == 2 and r == 3:
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(12)         
                print("Got damage")
            elif Useskill == 3 and r == 1:                  
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(12)
                print("Got damage")
            elif Useskill == 3 and r == 2:      
                player[0][3]['monster'].name,player[0][3]['monster'].Attack(10)   
                print("you have done damage")         
            elif Useskill == 3 and r == 3:
                player[0][3]['monster'].name,player[0][3]['monster'].Attack(0)
                print("Draw")
            elif Useskill >=4:
                break