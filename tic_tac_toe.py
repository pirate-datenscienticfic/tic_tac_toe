# Making of my 1st game (Tic_Tac_Toe) in python 




# Display board definning
def displayboard(board):
	# Board : outter-list
	for row in board:  #e1,e2,e3
		print()
		# Board : inner list
		for col in row:
			print(col, end=" ")
	print()




# Definning the update-board
def updateboard(board, r, c, sym):
	if r < 0 or r >= len(board):
		return False
	elif c < 0 or c >= len(board[r]):
		return False
	elif board[r][c] != "[ ]":
		return False

	# Update board
	board[r][c] = "["+ sym +"]"
	return True



# Definning is is full board
def isfull(board):
	for row in board:
		for col in row:
			if col == "[ ]": # "[ ]" is empty
				return False				
	return True




# Definning checkwin concept
def checkwin(board, sym):
	sym = "[" +sym + "]"  # x  : [x]
	
	# row check
	i = 0
	while i < 3:
		if board[i][0]==sym and board[i][1]==sym and board[i][2]==sym:
			return True
		i += 1

	# col check
	i = 0
	while i < 3:
		if board[0][i]==sym and board[1][i]==sym and board[2][i]==sym:
			return True
		i += 1

	# diagonal check
	if board[0][0]==sym and board[1][1]==sym and board[2][2]==sym:
		return True
	# reverse diagonal check
	if board[0][2]==sym and board[1][1]==sym and board[2][0]==sym:
		return True
	
	return  False



# Definning tic_tac_toe function
def tictactoe():
   # It is basically MATRIX(normally 3X3),
   # It can implemented as NESTED LIST, 
   # It contain Board = [e1,e2,e3] (having row & column)
   # And, each column has row itself so e1 = ["val"]*3 or e1 = ["val","val","val"] (this is done 3 times)

	# Making of board
	board = [["[ ]"]*3,["[ ]"]*3,["[ ]"]*3]
	# giving player
	players = []
	# define symbol
	symbol = ['X','O']
	# Adding 2 players and their name is list
	players.append(input(" Enter the Name of player-1 : "))
	players.append(input(" Enter the Name of player-2 : ")) 


	i = 0
	while i < 2:
		print("---Symbol for "+players[i] +" : "+ symbol[i])
		i += 1

	# Call for use_full board
	i = 0
	flag = 1
	
	while not isfull(board):
		displayboard(board)
		print(players[i] + " (" + symbol[i] + ") plays : ")
		r = int(input(" Enter row (0-2) : "))
		c = int(input(" Enter col (0-2) : ")) 

		# updating the board
		if updateboard(board, r, c, symbol[i]):
			if checkwin(board, symbol[i]):
				displayboard(board)
				print( players[i] +" with symbol (" + symbol[i] +") WINS !!! ")
				flag = 0
				break
			i = (i+1)%2		
		else:
			print(" Invalid move ")
		
	
	if flag == 1:
		displayboard(board)
		print(" Game Draws !!!")



# Definning main function
def main():
	# call to tic_tac_toe func.
	tictactoe()
   # Invoke main func.
main()