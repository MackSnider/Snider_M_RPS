from random import randint

choices = ["rock", "paper", "scissors"]


player_lives = 5
ai_lives = 5

total_lives = 5


player = input("Choose rock, paper or scissors: ")

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

elif (computer == "paper"):
	if (player == "scissors"):
		print("You Lose! I'm laughing at you")
		player_lives -= 1
	else:
		print("You Win! Amazing work")

elif (computer == "scissors"):
	if (player == "rock"):
		print("You Lose! That's honestly just sad")
		player_lives -= 1
	else:
		print("You Win! Looking good")

print("player lives:", player_lives)
print("ai lives:", ai_lives)