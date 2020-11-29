from gameComponents import gameVars 

def winorlose(status):
	# print("inside winorlose function; status is: ", status)

	if status == "won":
		pre_message = "You have won the battle! You are now the Supreme RPS Champion of the World. "
	else:
		pre_message = "You have been defeated! Sucks to suck. "

	# print("You", status, "! Would you like to play again?")
	# print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
	print(pre_message + "Would you like to play again?")

	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("So sad to see you go! Play again soon :)")
		exit()

	elif choice == "Y" or choice == "y":

		gameVars.player_lives = 3 
		gameVars.computer_lives = 3
		gameVars.player = False
	else:
		print("Please make a valid choice this time - Y or N")
		choice = input("Y / N: ")