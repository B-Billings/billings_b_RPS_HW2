from gameComponents import gameVars


def winorlose(status):
    print("you " + status)

    choice = input("Would you like to play again? y/n: ")
    
    if choice == "n":
        print("Peace! It was fun while it lasted!")
        exit()
    elif choice == "y":

        print("Thanks for choosing to play again!")
       
        gameVars.playerLives = 5
        gameVars.computerLives = 5
        gameVars.player = False
    