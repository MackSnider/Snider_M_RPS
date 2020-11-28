from random import randint

from gameComponents import gameVars, winLose


while gameVars.player == False:
	print("ROCK PAPER SCISSORS BATTLE TO THE DEATH")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Computer Lives:", gameVars.player_lives, "/", gameVars.total_lives)

	print("Choose your desired weapon!")
	print("You can also quit at any point by typing quit\n")

	gameVars.player = input("Choose rock, paper or scissors: \n")


	if gameVars.player == "quit":
		print("You chose to quit. That's quite unfortunate, don't you think?")
		exit()

	computer = gameVars.choices[randint(0, 2)]


	print("user chose: " + gameVars.player)

	print("AI chose: " + computer)

	if (computer == gameVars.player):
		print("tie")

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives -= 1
			print("You Lose! That's pretty unfortunate. Player Lives: ", player_lives)
		else:
			print("You Win! Congrats, winner")
			gameVars.computer_lives -= 1

	elif (computer == "paper"):
		if (gameVars.player == "scissors"):
			gameVars.player_lives -=1
			print("You Lose! I'm laughing at you. Player Lives: ", player_lives)
		else:
			print("You Win! Amazing work")
			gameVars.computer_lives -= 1

	elif (computer == "scissors"):
		if (gameVars.player == "rock"):
			gameVars.player_lives -= 1
			print("You Lose! That's honestly just sad. Player Lives: ", player_lives)
		else:
			print("You Won! Looking good")
			gameVars.computer_lives -= 1

	if gameVars.player_lives == 0:
		winLose.winorlose("lost")

	elif gameVars.computer_lives == 0:
		winLose.winorlose("won")

	else:
		gameVars.player = False

	print("player lives:", player_lives, "lives left")
	print("ai lives:", ai_lives, "lives left")