from gameComponents import gameVars, winLose

def gameRules():
    if gameVars.player == gameVars.computer:
        print("\033[34m"+ "tie! try again" "\033[39m")
        
    elif gameVars.player == "rock":
            if gameVars.computer == "paper":
                print("\033[31m"+"you lost!""\033[39m")
                gameVars.playerLives = gameVars.playerLives - 1
            else:
                print("\033[32m"+"you win!""\033[39m")
                gameVars.computerLives = gameVars.computerLives - 1
        
    elif gameVars.player == "paper":
            if gameVars.computer == "scissors":
                print("\033[31m"+"you lost!""\033[39m")
                gameVars.playerLives = gameVars.playerLives - 1
            else:
                print("\033[32m"+"you win!""\033[39m")
                gameVars.computerLives = gameVars.computerLives - 1
        
    elif gameVars.player == "scissors":
            if gameVars.computer == "rock":
                print("\033[31m"+"you lost!""\033[39m")
                gameVars.playerLives = gameVars.playerLives - 1
            else:
                print("\033[32m"+"you win!""\033[39m")
                gameVars.computerLives = gameVars.computerLives - 1