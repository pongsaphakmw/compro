import json
import characters
import random
def GAME_3(user_name):
    player = characters.Game_items.game_list()
    print("Game 3 question Ez")
    state = int(input("choose state(1-3):"))
    if state == 1:
        print("Welcome to State 1")
        items=["Which nation was the first to sail?",
        "What is the highest mountain in the world?",
        "Which country is the largest in the world?",
        "Who discovered the Americas?",
        "National Animal of Indonesia?"]
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
            x=random.choice(items)
            if  x=='Which nation was the first to sail?':
                print("Which nation was the first to sail?")
                y=input("The answer is ").lower()
                ans='egypt'
                if y==ans:player[0][1]['monster'].name,player[0][1]['monster'].Attack(10),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(20),print("You got damaged T^T \nThe correct answer is Egypt")
            elif x=='What is the highest mountain in the world?':
                print("What is the highest mountain in the world?")
                y=input("The answer is ").lower()
                ans='everest'
                if y==ans:player[0][1]['monster'].name,player[0][1]['monster'].Attack(10),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(20),print("You got damaged T^T \nThe correct answer is Everest")
            elif x=='Which country is the largest in the world?':
                print("Which country is the largest in the world?")
                y=input("The answer is ").lower()
                ans='russia'
                if y==ans:player[0][1]['monster'].name,player[0][1]['monster'].Attack(10),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(20),print("You got damaged T^T \nThe correct answer is Russia")
            elif x=='Who discovered the Americas?':
                print("Who discovered the Americas?")
                y=input("The answer is ").lower()
                ans='christopher columbus'
                if y==ans:player[0][1]['monster'].name,player[0][1]['monster'].Attack(10),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(20),print("You got damaged T^T \nThe correct answer is Christopher Columbus")

            elif x=='National Animal of Indonesia?':
                print("National Animal of Indonesia?")
                y=input("The answer is ").lower()
                ans='komodo dragon'
                if y==ans:player[0][1]['monster'].name,player[0][1]['monster'].Attack(10),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(20),print("You got damaged T^T \nThe correct answer is Komodo Dragon")   

    elif state==2 :
        print("Welcome to State 2")
        items=["What is the largest island in the world?",
        "Which ocean is the largest in the world?",
        "Which countries have the most citizens?",
        "Which country created the Statue of Liberty? ",
        "When was General Prayuth Jan-ocha appointed prime minister of The State of Thailand?"]
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
            x=random.choice(items)
            if x=='What is the largest island in the world?':
                print("What is the largest island in the world?")
                y=input("The answer is ").lower()
                ans='greenland'
                if y==ans:player[0][2]['monster'].name,player[0][2]['monster'].Attack(15),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(20),print("You got damaged T^T \nThe correct answer is Greenland")

            elif x=='Which ocean is the largest in the world?':
                print("Which ocean is the largest in the world?")
                y=input("The answer is ").lower()
                ans='pacific'
                if y==ans:player[0][2]['monster'].name,player[0][2]['monster'].Attack(15),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(20),print("You got damaged T^T \nThe correct answer is Pacific")

            elif x=='Which countries have the most citizens?':
                print("Which countries have the most citizens?")
                y=input("The answer is ").lower()
                ans='china'
                if y==ans:player[0][2]['monster'].name,player[0][2]['monster'].Attack(15),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(20),print("You got damaged T^T \nThe correct answer is China")

            elif x=='Which country created the Statue of Liberty?':
                print("Which country created the Statue of Liberty?")
                y=input("The answer is ").lower()
                ans='france'
                if y==ans:player[0][2]['monster'].name,player[0][2]['monster'].Attack(15),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(20),print("You got damaged T^T \nThe correct answer is France")

            elif x=='When was General Prayuth Jan-ocha appointed prime minister of The State of Thailand?':
                print("When was General Prayuth Jan-ocha appointed prime minister of The State of Thailand?")
                y=input("The answer is ").lower()
                ans='2014'
                if y==ans:player[0][2]['monster'].name,player[0][2]['monster'].Attack(15),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(20),print("You got damaged T^T \nThe correct answer is 2014")
    elif state==3:
        print("Welcome to State 3")
        items=["What is it,as big as an elephant, but not heavy?",
        "What is it when we sleep,it stands when we stand it sleeping?",
        "What's a couple nearby but never seen each other?",
        "What is it?.It is your,but others use it more than you.",
        "What grade will Nattanai and Koonsub get in FUNDAMENTALS OF COMPUTER PROGRAMMING?"]
        MaxHP_main = player[0][0]['main_char'].HP
        MaxHP_monster = player[0][4]['monster'].HP
        while 1:
            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
            print("%s  have HP %s "%(player[0][4]['monster'].name,player[0][4]['monster'].HP))
            if player[0][0]['main_char'].HP<=0:
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][4]['monster'].reset(MaxHP_monster)
                print("lose")
                break
            elif player[0][4]['monster'].HP<=0:
                player[0][0]['main_char'].reset(MaxHP_main)
                player[0][4]['monster'].reset(MaxHP_monster)
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
            x=random.choice(items)
            if x=='What is it,as big as an elephant, but not heavy?':
                print("What is it,as big as an elephant, but not heavy?")
                y=input("The answer is ").lower()
                ans='elephant shadow'
                if y==ans:player[0][4]['monster'].name,player[0][4]['monster'].Attack(10),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(25),print("You got damaged T^T \nThe correct answer is elephant shadow")

            elif x=='What is it when we sleep,it stands when we stand it sleeping?':
                print("What is it when we sleep,it stands when we stand it sleeping?")
                y=input("The answer is ").lower()
                ans='foot'
                if y==ans:player[0][4]['monster'].name,player[0][4]['monster'].Attack(10),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(25),print("You got damaged T^T \nThe correct answer is foot")

            elif x=='What is a couple nearby but never seen each other?':
                print("What is a couple nearby but never seen each other?")
                y=input("The answer is ").lower()
                ans='ears'
                if y==ans:player[0][4]['monster'].name,player[0][4]['monster'].Attack(10),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(25),print("You got damaged T^T \nThe correct answer is ears")

            elif x=='What is it?.It is your,but others use it more than you.':
                print("What is it?.It is your,but others use it more than you.")
                y=input("The answer is ").lower()
                ans='name'
                if y==ans:player[0][4]['monster'].name,player[0][4]['monster'].Attack(10),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(25),print("You got damaged T^T \nThe correct answer is name")

            elif x=='What grade will Nattanai and Koonsub get in FUNDAMENTALS OF COMPUTER PROGRAMMING?':
                print("What grade will Nattanai and Koonsub get in FUNDAMENTALS OF COMPUTER PROGRAMMING?")
                y=input("The answer is ").lower()
                ans='a'
                if y==ans:player[0][4]['monster'].name,player[0][4]['monster'].Attack(10),print("Attack!")
                else:player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(100),print("You got damaged T^T \nThe correct answer is A")