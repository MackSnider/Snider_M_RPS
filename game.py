from random import randint

choices = ["rock", "paper", "scissors"]


player_lives = 1
ai_lives = 1

total_lives = 1


def winorlose(status):
	# print("inside winorlose function; status is: ", status)

	if status == "won"
		pre_message = "You have won the battle! You are now the Supreme RPS Champion of the World"
	else:
		pre_message = "You have been defeated! Sucks to suck"

	# print("You", status, "! Would you like to play again?")
	# print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
	print(pre_message + "Would you like to play again?")
	
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("So sad to see you go! Play again soon :)")
		exit()

	elif choice == "Y" or choice == "y":

		global player_lives
		global ai_lives
		global player

		player_lives = 1 
		ai_lives = 1
		player = False

	else:
		print("Please make a valid choice this time - Y or N")
		choice = input("Y / N: ")

player = False

while player == False:
	print("ROCK PAPER SCISSORS BATTLE TO THE DEATH")
	print("Computer Lives:", ai_lives, "/", total_lives)
	print("Computer Lives:", player_lives, "/", total_lives)

	print("Choose your desired weapon!")
	print("You can also quit at any point by typing quit\n")

	player = input("Choose rock, paper or scissors: \n")


	if player == "quit":
		print("You chose to quit. That's quite unfortunate, don't you think?")
		exit()

	computer = choices[randint(0, 2)]


	print("user chose: " + player)

	print("AI chose: " + computer)

	if (computer == player):
		print("tie")

	elif (computer == "rock"):
		if (player == "scissors"):
			print("You Lose! That's pretty unfortunate.")
			player_lives -= 1
		else:
			print("You Win! Congrats, winner")
			ai_lives -= 1

	elif (computer == "paper"):
		if (player == "scissors"):
			print("You Lose! I'm laughing at you")
			player_lives -= 1
		else:
			print("You Win! Amazing work")
			ai_lives -= 1

	elif (computer == "scissors"):
		if (player == "rock"):
			print("You Lose! That's honestly just sad")
			player_lives -= 1
		else:
			print("You Won! Looking good")
			ai_lives -= 1

	if player_lives == 0:
		winorlose("lost")

		# print("You have been defeated! Sucks to suck. Would you like to test your luck by playing again?")
		# choice = input("Y / N? ")

		# if choice == "N" or choice == "n":
		# 	print("Wow! really??? Come back when you're ready for round 2")
		# 	exit()

		# elif choice == "Y" or choice == "y":
		# 	player_lives = 1 
		# 	ai_lives = 1
		# 	player = False

		# else:
		# 	print("Please make a valid choice this time - Y or N")
		# 	choice = input("Y / N")

	if ai_lives == 0:
		winorlose("won")

		# print("You have won the battle! You are now the Supreme RPS Champion of the World")
		# print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
		# print("Would you like to play again?")
		# choice = input("Y / N? ")

		# if choice == "N" or choice == "n":
		# 	print("Retire on top, that's what I'd do too! Take care :)")
		# 	exit()

		# elif choice == "Y" or choice == "y":
		# 	player_lives = 1 
		# 	ai_lives = 1
		# 	player = False

		# else:
		# 	print("Please make a valid choice this time - Y or N")
		# 	choice = input("Y / N")

	print("player lives:", player_lives, "lives left")
	print("ai lives:", ai_lives, "lives left")