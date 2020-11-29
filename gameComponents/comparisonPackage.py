from random import randint

from gameComponents import gameVars


computer = gameVars.choices[randint(0, 2)]

def comparison(status):

		if (computer == gameVars.player):
			print("tie")

		elif (computer == "rock"):
			if (gameVars.player == "scissors"):
				gameVars.player_lives -= 1
				print("You Lose! That's pretty unfortunate. Player Lives: ", gameVars.player_lives)
			else:
				print("You Win! Congrats, winner")
				gameVars.computer_lives -= 1

		elif (computer == "paper"):
			if (gameVars.player == "scissors"):
				gameVars.player_lives -=1
				print("You Lose! I'm laughing at you. Player Lives: ", gameVars.player_lives)
			else:
				print("You Win! Amazing work")
				gameVars.computer_lives -= 1

		elif (computer == "scissors"):
			if (gameVars.player == "rock"):
				gameVars.player_lives -= 1
				print("You Lose! That's honestly just sad. Player Lives: ", gameVars.player_lives)
			else:
				print("You Win! Looking good")
				gameVars.computer_lives -= 1

