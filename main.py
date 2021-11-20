import time
import threading
import tkinter as tk
from typing import Collection


root = tk.Tk()
root.geometry("664x623")
root.title("Chess")

frame1 = tk.Frame(root); frame1.pack()

turn =0
buttons = []

board = [[2, 1, 0, 0, 0, 0, 7, 8],
		[3, 1, 0, 0, 0, 0, 7, 9],
		[4, 1, 0, 0, 0, 0, 7, 10],
		[5, 1, 0, 0, 0, 0, 7, 12],
		[6, 1, 0, 0, 0, 0, 7, 11],
		[4, 1, 0, 0, 0, 0, 7, 10],
		[3, 1, 0, 0, 0, 0, 7, 9],
		[2, 1, 0, 0, 0, 0, 7, 8]]

pieces = {0:"   ",
		  1:"\u2659", # White pawn
		  2:"\u2656", # White rook
		  3:"\u2658", # White knight
		  4:"\u2657", # White bishop
		  5:"\u2655", # White queen
		  6:"\u2654", # White king
		  7:"\u265F", # Black pawn
		  8:"\u265C", # Black rook
		  9:"\u265E", # Black knight
		  10:"\u265D", # Black bishop
		  11:"\u265B", # Black queen
		  12:"\u265A"} # Black king

def print_board():
	for y in range(0, 8):
		for x in range(0, 8):
			print(pieces[board[y][x]], end=" ")
		print()

def checkPossibleMove(piece, origin, move):
	if piece == 1: # Check if white pawn can move forward
		if origin[1] == 1 and move[1] == 3 and board[move[0]][move[1]] == 0 and origin[0] == move[0]: return True # Check if pawn can move 2 squares
		if move[1] == origin[1] + 1 and board[move[0]][move[1]] == 0 and origin[0] == move[0]: return True # Check if pawn can move 1 square forward
		try: 
			if move[1] == origin[1] + 1 and move[0] == origin[0] + 1 and board[move[0]][move[1]] != 0: return True # Check if pawn can capture diagonally
		except: pass
		try:
			if move[1] == origin[1] + 1 and move[0] == origin[0] - 1 and board[move[0]][move[1]] != 0: return True # Check if pawn can capture diagonally
		except: pass
		return False
		# Add En passant
		# Add Promotion
		
	elif piece == 2 or piece == 8: # Check if rooks can move
		check = True
		if origin[1] == move[1]:
			yrange = [char for char in range(origin[0]+1, move[0])] if origin[0] < move[0] else [char for char in range(move[0]+1, origin[0])]
			for num in yrange:
				if board[num][origin[1]] == 0: pass # Check if the inbetween spaces are empty on the y-axis
				else: check = False
		if origin[0] == move[0]:
			xrange = [char for char in range(origin[1]+1, move[1])] if origin[1] < move[1] else [char for char in range(move[1]+1, origin[1])]
			for num in xrange:
				if board[origin[0]][num] == 0: pass	# Check if the inbetween spaces are empty on the x-axis
				else: check = False
		if not (origin[1] == move[1] or origin[0] == move[0]): check = False # Check if the move is in a straight line
		del yrange, xrange
		if check == True: del check; return True

	elif piece == 3 or piece == 9: # Check if knights can move
		if origin[0]-2 == move[0] and origin[1]-1 == move[1]: return True # Check if knight can move up 2, left 1
		if origin[0]-2 == move[0] and origin[1]+1 == move[1]: return True # Check if knight can move up 2, right 1
		if origin[0]+2 == move[0] and origin[1]-1 == move[1]: return True # Check if knight can move down 2, left 1
		if origin[0]+2 == move[0] and origin[1]+1 == move[1]: return True # Check if knight can move down 2, right 1
		if origin[0]-1 == move[0] and origin[1]+2 == move[1]: return True # Check if knight can move right 2, up 1
		if origin[0]+1 == move[0] and origin[1]+2 == move[1]: return True # Check if knight can move right 2, down 1
		if origin[0]-1 == move[0] and origin[1]-2 == move[1]: return True # Check if knight can move left 2, up 1
		if origin[0]+1 == move[0] and origin[1]-2 == move[1]: return True # Check if knight can move left 2, down 1

	elif piece == 4 or piece == 10: # white bishop
		check= True
		yrange = [char for char in range(origin[0]+1, move[0])] if origin[0] < move[0] else [char for char in range(move[0]+1, origin[0])]
		xrange = [char for char in range(origin[1]+1, move[1])] if origin[1] < move[1] else [char for char in range(move[1]+1, origin[1])]
		if len(yrange) == len(xrange):
			for num in range(len(yrange)):
				if board[yrange[num]][xrange[num]] == 0: pass
				else: check = False
		else: check = False
		del yrange, xrange
		if check == True: del check; return True

	elif piece == 5: # white queen
		pass



	elif piece == 6: # white king
		pass



	elif piece == 7: # Check if black pawn can move forward
		if origin[1] == 6 and move[1] == 4 and board[move[0]][move[1]] == 0 and origin[0] == move[0]: return True # Check if pawn can move 2 squares
		if move[1] == origin[1] - 1 and board[move[0]][move[1]] == 0 and origin[0] == move[0]: return True # Check if pawn can move 1 square forward
		try: 
			if move[1] == origin[1] - 1 and move[0] == origin[0] + 1 and board[move[0]][move[1]] != 0: return True # Check if pawn can capture diagonally
		except: pass
		try:
			if move[1] == origin[1] - 1 and move[0] == origin[0] - 1 and board[move[0]][move[1]] != 0: return True # Check if pawn can capture diagonally
		except: pass
		return False

	return False


class CreateButton:

	originCoords = ()
	originNumber = None

	def __init__(self, number, coords):
		self.number = number
		self.coords = coords
		self.button = tk.Button(frame1, text=pieces[board[coords[0]][coords[1]]], font='Helvetica 18 bold', command=self.button_click, width=5, height=2, relief="solid", borderwidth=1)
		# self.button = tk.Button(frame1, text=number, font='Helvetica 18 bold', command=self.button_click, width=5, height=2)

	def __flashRed(self):
		self.button.config(bg="red"); 
		time.sleep(0.3); 
		self.button.config(bg="SystemButtonFace")

	def button_click(self):
		global turn
		thread = threading.Thread(target=self.__flashRed)

		if CreateButton.originCoords == self.coords:
			CreateButton.originCoords = ()
			CreateButton.originNumber = None
			self.button.config(bg="SystemButtonFace")
			return

		if CreateButton.originCoords == ():
			# Check if space is empty
			if board[self.coords[0]][self.coords[1]] == 0:
				thread.start()
				return
			# Check if piece is white on white turn
			if board[self.coords[0]][self.coords[1]] in range(1, 7):
				if turn != 0:
					thread.start()
					return
			# Check if piece is black on black turn
			elif board[self.coords[0]][self.coords[1]] in range(7, 13):
				if turn != 1:
					thread.start()
					return


			CreateButton.originCoords = self.coords
			CreateButton.originNumber = self.number
			self.button.config(bg="green")

		else:
			if checkPossibleMove(board[CreateButton.originCoords[0]][CreateButton.originCoords[1]], CreateButton.originCoords, self.coords) != True:
				thread.start()
				return

			# Check if piece is same colour
			if board[self.coords[0]][self.coords[1]] in range(1, 7) and board[CreateButton.originCoords[0]][CreateButton.originCoords[1]] in range(1, 7):
				thread.start()
				return
			if board[self.coords[0]][self.coords[1]] in range(7, 13) and board[CreateButton.originCoords[0]][CreateButton.originCoords[1]] in range(7, 13):
				thread.start()
				return

			# Successful move
			board[self.coords[0]][self.coords[1]] = board[CreateButton.originCoords[0]][CreateButton.originCoords[1]]
			self.button.config(text=pieces[board[self.coords[0]][self.coords[1]]])
			buttons[(CreateButton.originNumber)].button.config(bg="SystemButtonFace")
			board[CreateButton.originCoords[0]][CreateButton.originCoords[1]] = 0
			buttons[(CreateButton.originNumber)].button.config(text=pieces[0])
			CreateButton.originCoords = ()
			CreateButton.originNumber = None
			turn = 0 if turn == 1 else 1


# Create Buttons
createCount = 0
for y in range(0, 8):
	for x in range(0, 8):
		buttons.append(CreateButton(createCount, (y, x)))
		createCount += 1
del createCount

# Place buttons
placeCount = 0
for x in range(0, 8):
	for y in range(0, 8):
		buttons[placeCount].button.grid(row=x, column=y)
		placeCount += 1
del placeCount

root.mainloop()
