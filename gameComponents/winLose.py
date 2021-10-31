def winorLose(status):
    print("You " + status + "! Would you like to play again?")
    choice = input(" Y / N?")

    global playerLives
    global computerLives
    global player

    if choice == "n":
        print("better luck next time!")
        exit()
    else:
        playerLives = 5
        computerLives = 5
        player = False