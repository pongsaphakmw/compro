import json
import characters
from random import randint

player = characters.Game_items.game_list()

print("Game 2 ....")
state = int(input("choose state :"))
if state == 1:
    print("Welcome to State 1")
    print("Calculate the equation to get rid of monsters!!")
    while 1:
        print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
        print("%s  have HP %s "%(player[0][1]['monster'].name,player[0][1]['monster'].HP))
        if player[0][0]['main_char'].HP<=0:
            print("lose")
            break
        elif player[0][1]['monster'].HP<=0:
            print("won")
            break

        for i in range(1):
            x = randint(1,90)
            y = randint(1,90)
            randomproblem = x+y
            print("%d + %d"%(x, y))
            #print(randomproblem)
            answer = int(input("In put your answer: "))
            if answer == randomproblem:
                print("Correct")
                player[0][1]['monster'].name,player[0][1]['monster'].Attack(10)
                print("you have done damage")
                break
            elif answer != randomproblem:
                print("Try again")
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)
                print("Got damage")
                break
elif state == 2:
    print("Welcome to State 2")
    print("Calculate the equation to get rid of monsters!!")
    while 1:
        print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
        print("%s  have HP %s "%(player[0][2]['monster'].name,player[0][2]['monster'].HP))
        if player[0][0]['main_char'].HP<=0:
            print("lose")
            break
        elif player[0][2]['monster'].HP<=0:
            print("won")
            break

        for i in range(1):
            x = randint(1,90)
            y = randint(1,90)
            randomproblem = x-y
            print("%d - %d"%(x, y))
            #print(randomproblem)
            answer = int(input("In put your answer: "))
            if answer == randomproblem:
                print("Correct")
                player[0][2]['monster'].name,player[0][2]['monster'].Attack(10)
                print("you have done damage")
                break
            elif answer != randomproblem:
                print("Try again")
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)
                print("Got damage")
                break
elif state == 3:
    print("Welcome to State 3")
    print("Calculate the equation to get rid of monsters!!")
    while 1:
        print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
        print("%s  have HP %s "%(player[0][4]['monster'].name,player[0][4]['monster'].HP))
        if player[0][0]['main_char'].HP<=0:
            print("lose")
            break
        elif player[0][4]['monster'].HP<=0:
            print("won")
            break

        for i in range(1):
            x = randint(1,90)
            y = randint(1,90)
            randomproblem = x*y
            print("%d * %d"%(x, y))
            #print(randomproblem)
            answer = int(input("In put your answer: "))
            if answer == randomproblem:
                print("Correct")
                player[0][4]['monster'].name,player[0][4]['monster'].Attack(10)
                print("you have done damage")
                break
            elif answer != randomproblem:
                print("Try again")
                player[0][0]['main_char'].name,player[0][0]['main_char'].Attack(10)
                print("Got damage")
                break
    