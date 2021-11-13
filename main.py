from random import randint
from gameComponents import gameRules, winLose, gameVars

print("\033[32m"+"==============================================================")
print("\033[31m"+"======= Welcome to the Rock Paper Scissors Python Game =======")
print("\033[32m"+"==============================================================")
print("\033[31m"+"====== The Computer and Player both have 5 Lives each! =======")
print("\033[31m"+"========== Whoevers lives hit 0 first is the loser! ==========")
print("\033[32m"+"==============================================================")
print("\033[39m") #makes colour of text white again
while gameVars.player is False:
    print("\033[39m")
    gameVars.player = input("Choose your weapon: rock, paper or scissors:")
    gameVars.computer = gameVars.choices[randint(0, 2)]
   
    print("==============================================================")

    print("\033[36m"+"player chose: " + gameVars.player)
    print("\033[35m"+"computer chose: " + gameVars.computer)
    
    gameRules.gameRules()
    
    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    print("==============================================================")

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False