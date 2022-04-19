from math import e
from unicodedata import name



from pip import main
import characters
from random import randint
player = characters.Game_items.game_list()
def GAME_1():
    print("Game 1 ....") 
    state = int(input("choose state :"))
    if state == 1:  
        print("Welcome to State 1")
        print("Attack  = 1")
        print("Counter = 2")
        print("Magic   = 3")
        while 1:
            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
            print("%s  have HP %s "%(player[0][1]['monster'].name,player[0][1]['monster'].HP))     
            if player[0][0]['main_char'].HP<=0:
                print("lose")
                break
            elif player[0][1]['monster'].HP<=0:
                print("won")
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
        while 1:
            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
            print("%s  have HP %s "%(player[0][2]['monster'].name,player[0][2]['monster'].HP))     
            if player[0][0]['main_char'].HP<=0:
                print("lose")
                break
            elif player[0][2]['monster'].HP<=0:
                print("won")
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
        while 1:
            print("%s your  HP is %s "%(player[0][0]['main_char'].name,player[0][0]['main_char'].HP))
            print("%s  have HP %s "%(player[0][3]['monster'].name,player[0][3]['monster'].HP))     
            if player[0][0]['main_char'].HP<=0:
                print("lose")
                break
            elif player[0][3]['monster'].HP<=0:
                print("won")
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
        
#GAME_1()
#while True:
    #if GAME_1 !=0:
       # GAME_1()
 #   else:
    #    break