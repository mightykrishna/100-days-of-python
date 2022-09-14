#display art
from image import logo
from image import vs
from data import data
import random

def format_data(choice):
    choice_name=choice_a["name"]
    choice_des=choice_a["description"]
    choice_country=choice_a["country"]
    print(f"{choice_name}, a {choice_des}, from{choice_country}")

def check(guess,a_follower,b_follower):
    if a_follower>b_follower :
        return guess=="a"
    else:
        return guess=="b"
            

print (logo)

score=0
#generate a random account form the game data
while True:  
    choice_a=random.choice(data)
    choice_b=random.choice(data)
    if(choice_a==choice_b):
        choice_b=random.choice(data)

    print(f"compare a:{format_data(choice_a)}")
    print(vs)
    print(f"compare B: {format_data(choice_b)}")
    #ask user for a guess
    guess=input("who has more followers on instagram A or B").lower()


    #get follow count of each account

    a_follower=choice_a["follower_count"]
    b_follower=choice_b["follower_count"]
    #use if statement to check if user is correct
    is_correct=check(guess,a_follower,b_follower)
    #give user a feedback
    
    if is_correct:
        score+=1
        print(f"you are right :your score is {score}")
    else:
        print(f"you are wrong: your score is {score} ")
    #score keeping

    #make the game reapeatable
    play=input("if u want to play to again press  y or n ").lower()
    if play=="y":
        continue
    else:
        break

print(f"game ended the score is {score}")
#making account at position B become the next account at position B

#clear the screen between rounds