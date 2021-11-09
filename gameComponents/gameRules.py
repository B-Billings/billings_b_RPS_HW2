from gameComponents import gameVars, winLose

def gameRules():
    if gameVars.player == gameVars.computer:
        print("tie! try again")
        
    elif gameVars.player == "rock":
            if gameVars.computer == "paper":
                print("you lose!")
                gameVars.playerLives = gameVars.playerLives - 1
            else:
                print("you win!")
                gameVars.computerLives = gameVars.computerLives - 1
        
    elif gameVars.player == "paper":
            if gameVars.computer == "scissors":
                print("you lose!")
                gameVars.playerLives = gameVars.playerLives - 1
            else:
                print("you win!")
                gameVars.computerLives = gameVars.computerLives - 1
        
    elif gameVars.player == "scissors":
            if gameVars.computer == "rock":
                print("you lose!")
                gameVars.playerLives = gameVars.playerLives - 1
            else:
                print("you win!")
                gameVars.computerLives = gameVars.computerLives - 1