import random as rnd
import sys

"""This is a text based game of tic-tac-toe made by Zachary Gillmore
There is no way to win the ai will always make you lose or end in a draw"""
board = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
def print_board():
	"""prints the current board state"""
	print("    1   2   3  ")
	print("  -------------")
	print(f"1 | {board[0][0]} | {board[0][1]} | {board[0][2]} |")
	print("  -------------")
	print(f"2 | {board[1][0]} | {board[1][1]} | {board[1][2]} |")
	print("  -------------")
	print(f"3 | {board[2][0]} | {board[2][1]} | {board[2][2]} |")
	print("  -------------\n")

def check_win(p):
	"""Checks if the value of'p' won """
	for i in range(3):
		if(p == board[i][0] and p == board[i][1] and p == board[i][2]):
			return True
	for i in range(3):
		if(p == board[0][i] and p == board[1][i] and p == board[2][i]):
			return True
	if(p == board[0][0] and p == board[1][1] and p == board[2][2]):
		return True
	elif(p == board[2][0] and p == board[1][1] and p == board[0][2]):
		return True
	else:
		return False

def possible_win(p):
	"""returns"""
	for i in range(3):
		rc1,rc2 = 0,0
		cord1,cord2 = 0, 0
		for j in range(3):
			if(p == board[i][j]):
				rc1 += 1
			elif(board[i][j] == ' '):
				cord1 = (i,j)
			else:
				rc1 = 0
			if(p == board[j][i]):
				rc2 += 1
			elif(board[j][i] == ' '):
				cord2 = (j,i)
			else:
				rc2 = 0
		if(rc1 == 2 and cord1 != 0):
			return cord1
		elif(rc2 == 2 and cord2 != 0):
			return cord2
	rc3,rc4 = 0,0
	cord3,cord4 = 0, 0
	if(p == board[0][0]):
		rc3 += 1
	if(p == board[1][1]):
		rc3 += 1
		rc4 += 1
	if(p == board[2][2]):
		rc3 += 1
	if(p == board[2][0]):
		rc4 += 1
	if(p == board[0][2]):
		rc4 += 1
	if(' ' == board[0][0]):
		cord3 = (0,0)
	if(' ' == board[1][1]):
		cord3 = (1,1)
		cord4 = (1,1)
	if(' ' == board[2][2]):
		cord3 = (2,2)
	if(' ' == board[2][0]):
		cord4 = (2,0)
	if(' ' == board[0][2]):
		cord4 = (0,2)
	if(rc3 == 2 and cord3 != 0):
			return cord3
	elif(rc4 == 2 and cord4 != 0):
			return cord4
	return "No possible wins"
def find_e_spaces():
	"""finds and returns any empty spaces on the board"""
	e_space = []
	for i in range(3):
		for j in range(3):
			if(board[i][j] == ' '):
				e_space.append((i,j))
	return e_space

def ai_move(p):
	"""returns the ai's move"""
	e_space = find_e_spaces()
	cord = possible_win(p)
	if(cord == "No possible wins"):
		cord = possible_win(player)
	if(cord != "No possible wins"):
		return cord
	if(p == 'O'):
		if((1,1) in e_space):
			return (1,1)
		elif(board[1][1] == 'X'):
			if((0,0) in e_space and (2,2) in e_space):
				return (0,0)
			elif((2,0) in e_space and (0,2) in e_space):
				return (2,0)
			elif((0,2) in e_space and (2,0) in e_space):
				return (0,2)
			elif((2,2) in e_space and (0,0) in e_space):
				return (2,2)
			elif((0,1) in e_space and (2,1) in e_space):
				return (0,1)
			elif((1,0) in e_space and (1,2) in e_space):
				return (1,0)
			elif((1,2) in e_space and (1,0) in e_space):
				return (1,2)
			elif((2,1) in e_space and (0,1) in e_space):
				return (2,1)
		elif((0,1) in e_space and (2,1) in e_space):
			return (0,1)
		elif((1,0) in e_space and (1,2) in e_space):
			return (1,0)
		elif((1,2) in e_space and (1,0) in e_space):
			return (1,2)
		elif((2,1) in e_space and (0,1) in e_space):
			return (2,1)
		elif((0,0) in e_space and (2,2) in e_space):
			return (0,0)
		elif((2,0) in e_space and (0,2) in e_space):
			return (2,0)
		elif((0,2) in e_space and (2,0) in e_space):
			return (0,2)
		elif((2,2) in e_space and (0,0) in e_space):
			return (2,2)
		else:
			return rnd.choice(e_space)
	elif(((0,0) in e_space)):
		return (0,0)
	elif((0,1) in e_space and (0,2) in e_space):
		return (0,2)
	elif((1,0) in e_space and (2,0) in e_space):
		return (2,0)
	elif((2,2) in e_space):
		return (2,2)
	else:
		return rnd.choice(e_space)

def player_turn(p):
	"""Asks the player for a move and performs it"""
	while(True):
		try:
			p_move = input("Enter a coordinate format 'row,column'\n")
			if(p_move == "q" or p_move ==  "quit"):
				sys.exit()
			p_move = [int(i)-1 for i in p_move.split(",")]
			p_move = (p_move[0],p_move[1])
			if(p_move in find_e_spaces()):
				board[p_move[0]][p_move[1]] = p
				print_board()
				break
			else:
				print("Position not empty!")
		except SystemExit:
			sys.exit()
		except:
			print("Error you must enter two numbers seperated by a ','\n")
player = input("Do you want to be X or O(X goes first): ").upper()
op = ''
while(True):
	"""main loop of the game."""
	if(player in {"X","O"}):
		break
	else:
		player = input("Do you want to be X or O(X goes first): ").upper()
if(player == 'X'):
	op = 'O'
else: op = 'X'
print_board()
while(True):
	if(check_win(player)):
		print("You win!")
		x = input("Press enter to quit: ")
		break
	elif(check_win(op)):
		print("You lose!")
		x = input("Press enter to quit: ")
		break
	elif(len(find_e_spaces()) < 1):
		print("Draw!")
		x = input("Press enter to quit: ")
		break
	if(player == 'X'):
		player_turn(player)
		if(check_win(player)):
			print("You win!")
			x = input("Press enter to quit: ")
			break
		elif(check_win(op)):
			print("You lose!")
			x = input("Press enter to quit: ")
			break
		elif(len(find_e_spaces()) < 1):
			print("Draw!")
			x = input("Press enter to quit: ")
			break
		ai = ai_move(op)
		board[ai[0]][ai[1]] = op
		print("Oponents turn!")
		print_board()
	else:
		ai = ai_move(op)
		board[ai[0]][ai[1]] = op
		print("Oponents turn!")
		print_board()
		if(check_win(player)):
			print("You win!")
			x = input("Press enter to quit: ")
			break
		elif(check_win(op)):
			print("You lose!")
			x = input("Press enter to quit: ")
			break
		elif(len(find_e_spaces()) < 1):
			print("Draw!")
			x = input("Press enter to quit: ")
			break
		player_turn(player)
