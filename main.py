from random import randint
player = input("Chose rock, paper or scissors")
player = input("player chose: " + player)
print("player chose: " + player)
choices = ["rock", "paper", "scissors"]
computer = choices[randint(0,2)]
print("computer chose" + computer)
if (player == "rock"):
    if (computer == "paper"):
        print ("you lose")
    elif (computer == "scissors"):
        print("you win")
    else:
        print("tie try again")

elif (player == "paper"):
    if (computer == "scissors"):
        print("you lose")
    elif (computer == "rock"):
        print ("you win!")
    else:
        print("tie!try again")

elif (player == "scissors"):
    if (computer == "rock"):
        print("you lose")
    elif (computer == "paper"):
        print ("you win!")
    else:
        print("tie!try again")
