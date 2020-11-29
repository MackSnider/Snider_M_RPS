from random import randint

from gameComponents import gameVars, winLose, comparisonPackage


while gameVars.player == False:
	print("ROCK PAPER SCISSORS! BATTLE TO THE DEATH")
	print("|||||||||||||||||||||||||||||||||||||||||")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("|||||||||||||||||||||||||||||||||||||||||")
	print("Choose your desired weapon!")
	print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
	print("You can also quit at any point by typing quit\n")

	gameVars.player = input("Choose rock, paper or scissors: \n")


	if gameVars.player == "quit":
		print("You chose to quit. That's quite unfortunate, don't you think?")
		exit()

	computer = gameVars.choices[randint(0, 2)]


	print("user chose: " + gameVars.player)

	print("AI chose: " + computer)


	comparisonPackage.comparison(gameVars.player)


	if gameVars.player_lives == 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False

	print("player lives:", gameVars.player_lives, "lives left")
	print("computer lives:", gameVars.computer_lives, "lives left")