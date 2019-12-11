from gameFunctions import gameVars, winlose

def comparechoices(c_omputer,p_layer):
	if p_layer == "quit":
			exit()
	elif c_omputer == p_layer:
		print("tie! no one wins, play again")
	elif p_layer == "rock":
		if c_omputer == "paper":
			print("You lose!", c_omputer, "covers", p_layer, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", p_layer, "smashes", c_omputer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif p_layer == "paper":
		if c_omputer == "scissors":
			print("You lose!", c_omputer, "cuts", p_layer, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", p_layer, "covers", c_omputer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif p_layer == "scissors":
		if c_omputer == "rock":
			print("You lose!", c_omputer, "smashes", p_layer, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", p_layer, "cuts", c_omputer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("=====================================")
		print("That's not a valid choice, try again")
		print("=====================================")
