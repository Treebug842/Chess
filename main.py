import time
import threading
import tkinter as tk
from typing import Collection


root = tk.Tk()
root.geometry("680x640")
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

# pieceType = {0:"empty",
#             1:"pawn",
#             2:"rook",
#             3:"knight",
#             4:"bishop",
#             5:"queen",
#             6:"king",
#             7:"pawn",
#             8:"rook",
#             9:"knight",
#             10:"bishop",
#             11:"queen",
#             12:"king"}

def print_board():
    for y in range(0, 8):
        for x in range(0, 8):
            print(pieces[board[y][x]], end=" ")
        print()

def checkPossibleMove(piece, origin, move):
    if piece == 0: return False


    elif piece == 1: # white pawn
        pass



    elif piece == 2: # white rook
        pass



    elif piece == 3: # white knight
        pass



    elif piece == 4: # white bishop
        pass



    elif piece == 5: # white queen
        pass



    elif piece == 6: # white king
        pass



    elif piece == 7: # black pawn
        pass



    elif piece == 8: # black rook
        pass



    elif piece == 9: # black knight
        pass



    elif piece == 10: # black bishop
        pass



    elif piece == 11: # black queen
        pass



    elif piece == 12: # black king
        pass














class CreateButton:

    originCoords = ()
    originNumber = None

    def __init__(self, number, coords):
        self.number = number
        self.coords = coords
        self.button = tk.Button(frame1, text=pieces[board[coords[0]][coords[1]]], font='Helvetica 18 bold', command=self.button_click, width=5, height=2)

    def __flashRed(self):
        self.button.config(bg="red"); 
        time.sleep(0.3); 
        self.button.config(bg="SystemButtonFace")

    def button_click(self):
        global turn
        thread = threading.Thread(target=self.__flashRed)

        if CreateButton.originCoords == ():

            if board[self.coords[0]][self.coords[1]] == 0:
                thread.start()
                return
            
            if board[self.coords[0]][self.coords[1]] in range(1, 7):
                if turn != 0:
                    thread.start()
                    return

            elif board[self.coords[0]][self.coords[1]] in range(7, 13):
                if turn != 1:
                    thread.start()
                    return


            CreateButton.originCoords = self.coords
            CreateButton.originNumber = self.number
            self.button.config(bg="green")

        else:
            # self.button.config(bg="red")
            


            # check if move is valid


            
            board[self.coords[0]][self.coords[1]] = board[CreateButton.originCoords[0]][CreateButton.originCoords[1]]
            self.button.config(text=board[self.coords[0]][self.coords[1]])

            buttons[CreateButton.OriginNumber].button.config(bg="SystemButtonFace")
            board[CreateButton.originCoords[0]][CreateButton.originCoords[1]] = 0
            buttons[CreateButton.OriginNumber].button.config(text=pieces[0])

            CreateButton.originCoords = ()
            CreateButton.originNumber = None

            turn = 0 if turn == 1 else 1




createCount = 0
for y in range(0, 8):
    for x in range(0, 8):
        buttons.append(CreateButton(createCount, (y, x)))
        createCount += 1
del createCount

placeCount = 0
for x in range(0, 8):
    for y in range(0, 8):
        buttons[placeCount].button.grid(row=x, column=y)
        placeCount += 1
# del placeCount


print_board()

root.mainloop()

