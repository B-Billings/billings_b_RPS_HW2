from random import randint
from gameComponents import gameRules, winLose, gameVars

print("=======Welcome to the Rock Paper Scissors Python Game=======")
while gameVars.player is False:
    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]
    
    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)
    
    if gameVars.player == gameVars.computer:
        gameRules.gameRules("tie")
    
    elif gameVars.player == "rock":
        gameRules.gameRules("rock")
    
    elif gameVars.player == "paper":
        gameRules.gameRules("paper")
    
    elif gameVars.player == ("scissors"):
        gameRules.gameRules("scissors")
    
    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False