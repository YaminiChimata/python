import random

user_won=0
cpu_won=0
choice=["rock","paper","scissors"]
while True:
    user_input=input("enter rock/paper/scissors or q to quit the game:").lower()
    if user_input=="q":
        break
    if user_input not in ["rock","paper","scissors"]:
        continue
    random_num=random.randint(0,2)
    cpu_choice=choice[random_num]
    print("cpu picked ",cpu_choice)
    if user_input=="rock" and cpu_choice=="scissors":
        print("you won🎉")
        user_won+=1
    elif user_input=="paper" and cpu_choice=="rock":
        print("you won🎉")
        user_won+=1
    elif user_input=="scissors" and cpu_choice=="paper":
        print("you won🎉")
        user_won+=1    
    elif user_input==cpu_choice:
        print("Draw ")
    else:
        print("you lost")
        cpu_won+=1
print("GAME OVER")
print("you won",user_won,"times")
print("CPU won",cpu_won,"times")
