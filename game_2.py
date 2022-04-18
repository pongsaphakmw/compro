import json
import characters
from random import randint

player = characters.Game_items.game_list()

print("Game 2 ....")
state = int(input("choose state : "))
if state == 1:
    print("Welcome to State 1")
    print("Calculate the equation to get rid of monsters!!")
    print("------------------------------")
    while 1:
        print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
        print("%s  have HP %s "%(player[0][1]['monster'].name,player[0][1]['monster'].HP))
        print("------------------------------")
        if player[0][0]['main_char'].HP<=0:
            print("\tlose")
            break
        elif player[0][1]['monster'].HP<=0:
            print("\twon")
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
    while 1:
        print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
        print("%s  have HP %s "%(player[0][2]['monster'].name,player[0][2]['monster'].HP))
        print("------------------------------")
        if player[0][0]['main_char'].HP<=0:
            print("\tlose")
            break
        elif player[0][2]['monster'].HP<=0:
            print("\twon")
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
    while 1:
        print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
        print("%s  have HP %s "%(player[0][4]['monster'].name,player[0][4]['monster'].HP))
        print("------------------------------")
        if player[0][0]['main_char'].HP<=0:
            print("\tlose")
            break
        elif player[0][4]['monster'].HP<=0:
            print("\twon")
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
    