# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	# set player to True
	print("**********************************")
	print("Computer lives: ", gameVars.computer_lives, "/", gameVars.total_lives,"\n")
	print("Player lives: ", gameVars.player_lives, "/", gameVars.total_lives, "\n")
	print("Choose your weapon!\n")
	print("**********************************")


	print("=====================================")
	gameVars.player = input("choose rock, paper or scissors: ")
	gameVars.player = gameVars.player.lower()

	print("computer chose ", gameVars.computer, "\n")
	print("player chose ", gameVars.player, "\n")

	print("=====================================")

	compare.comparechoices(gameVars.computer, gameVars.player)

	# if gameVars.player == "quit":
	# 	exit()
	# elif gameVars.computer == gameVars.player:
	# 	print("tie! no one wins, play again")

	# elif gameVars.player == "rock":
	# 	if gameVars.computer == "paper":
	# 		print("You lose!", gameVars.computer, "covers", gameVars.player, "\n")
	# 		gameVars.player_lives = gameVars.player_lives - 1
	# 	else:
	# 		print("You win!", gameVars.player, "smashes", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives - 1

	# elif gameVars.player == "paper":
	# 	if gameVars.computer == "scissors":
	# 		print("You lose!", gameVars.computer, "cuts", gameVars.player, "\n")
	# 		gameVars.player_lives = gameVars.player_lives - 1
	# 	else:
	# 		print("You win!", player, "covers", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives - 1

	# elif gameVars.player == "scissors":
	# 	if gameVars.computer == "rock":
	# 		print("You lose!", gameVars.computer, "smashes", gameVars.player, "\n")
	# 		gameVars.player_lives = gameVars.player_lives - 1
	# 	else:
	# 		print("You win!", player, "cuts", gameVars.computer, "\n")
	# 		gameVars.computer_lives = gameVars.computer_lives - 1

	# else:
	# 	print("=====================================")
	# 	print("That's not a valid choice, try again")
	# 	print("====================================

	# handle all lives lost for player or AI
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]	

