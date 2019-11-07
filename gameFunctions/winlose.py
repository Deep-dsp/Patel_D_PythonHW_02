from random import randint
# define a python function that takes an argument
def winorlose(status): 
	# status will be either won or lost - you're passing this in as an argument
	print("called win or lose")
	print("************************")

	print("You", status + "! Would you like to play again?")

	choice = input("Y / N: ")
	print("=============")
	print(choice)
	print("=============")

	if (choice is "N") or (choice is "n"):
		print("**********************")
		print("You chose to quit.")
		exit()
		print("**********************")

	elif (choice is "Y") or (choice is "y"):
		# reset the game so that we can start all over again
		# this will break, currently - we will fix this next class
		
		global computer
		global computer_lives
		global player
		global player_lives

		player_lives = 2
		computer_lives = 2
		player = False
		computer = choices[randint(0,2)]
	
	else:
		# not a y or n, so make the user pick a valid choice
		print("make a valid choice, Y or N")
		# this is recursion - call a function
		# from inside itself. Basically just re-up the choice
		# and force the user to pick yes or no (y or n)
		winorlose(status)