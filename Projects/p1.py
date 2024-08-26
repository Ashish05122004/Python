'''
0-snake
1-water
2-gun
'''
import random

while True:
    userChoice = input("Enter your choice (s,w,g): ")
    if(userChoice == "0"):
        print("game is terminated")
        break
    comp = random.choice([0,1,2])
    dict ={"s":0,"w":1,"g":2}
    user = dict[userChoice]
    newDict={0:"snake",1:"water",2:"gun"}
    print(f"you chose {newDict[user]} computer chose {newDict[comp]}")
    if(comp == user):
        print("It's draw")
    else:
        # if(comp ==0 and user ==1):
        #     print("You lose!!")
        # elif(comp ==0 and user ==2):
        #     print("you win")
        # elif(comp ==1 and user ==0):
        #     print("you win")
        # elif(comp ==1 and user ==2):
        #     print("you lose!!")
        # elif(comp ==2 and user ==0):
        #     print("you lose!!")
        # elif(comp ==2 and user ==1):
        #     print("you win")
        # else:
        #     print("Something went wrong!!")
        
        if(comp-user == -2 or comp-user == 1 or comp-user == 1):
            print("you win")
        else:
            print("you lose!!")