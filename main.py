from random import choice, randint
from gameComponents import winLose

choices = ["rock", "paper", "scissors"]

player = False

# the lives decrease when round is lost
playerLives = 5
computerLives = 5

while player is False:

    player = input("Chose your weapon: rock, paper or scissors: ")
    computer = choices[randint(0,2)]

    print("player chose:  " + player)
    print("computer chose:  " + computer)

    if computer == player:
        print("tie try again")
    elif (player == "rock"):
        if (computer == "paper"):
            print ("you lose")
            playerLives = playerLives -1
        else:
            print("you win!")
            computerLives = computerLives -1

    elif player == "paper":
        if computer== "scissors":
            print("you lose")
            playerLives = playerLives -1
        else:
            print("you win")
            computerLives = computerLives -1

    elif player == "paper":
        if computer == "scissors":
            print("you lose")
            playerLives = playerLives -1
        else:
            print("you win!")
            computerLives = computerLives -1

    elif player == "scissors":
        if computer == "rock":
            print("you lose!")
            playerLives = playerLives -1
        else:
            print("you win!")
            computerLives = computerLives -1

    print("player life count " + str(playerLives))
    print("player life count " + str(computerLives))

    if playerLives == 0:
        winorlose("lost")

        print("you lost! would you like to play again?")
        choice = input(" Y / N ")

        if choice == "n":
            print*"better luck nexttime!"
            exit()
        
        else:
            playerLives = 5
            computerLives = 5
            player = False

    elif computerLives == 0:
        winorlose("won")
        
        print("you won! Would you like to play again?")
        choice = input(" Y / N ")

        if choice == "n":
            print("better luck next time!")
            exit()

        else:
            playerLives = 5
            computerLives = 5
            player = False

