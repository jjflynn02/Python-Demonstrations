import sys
from random import randint

board = []

for i in range(0,5):
	board.append(["O"]*5)

#print (board)

def print_board(board):
	for row in board:
		hold = (" ").join(row)
		print (hold)
	return board

print_board(board)

def random_row(board):
	return randint(0, len(board)-1)

def random_col(board):
	return randint(0, len(board)-1)


ship_row = random_row(board)
ship_col = random_col(board)

print(ship_row, ship_col)

for turn in range(4):
	print("Turn", turn +1 )
	guess_row = int(input("Guess Row: "))
	guess_col = int(input("Guess Col: "))

	if guess_row == ship_row and guess_col == ship_col:
		print ("Congradulations! You sank my battleship!")
		break

	elif guess_row not in range(5) or guess_col not in range(5):
		print("Oops, that's not even in the ocean!")

	elif board[guess_row][guess_col] == "X":
		print("You guessed that one already.")

	elif guess_row != ship_row or guess_col != ship_col:
		print ("You missed my battleship!")
		board[guess_row][guess_col] = "X"
		print_board(board)
		if turn >= 3:
			print("Game Over")


	#else:
		#print("You missed my battleship!")



