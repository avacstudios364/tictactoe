from tkinter import *
import random
from functools import partial
from tkinter import messagebox
from copy import deepcopy

sign = 0
global board
board = [['' for x in range(3)] for i in range(3)]

print(board)

def winner(b,l):
    return(
        #Horozontal wins
        (b[0][0] = 1 and b[0][1] = 1 and b[0][2] = 1) or
        (b[1][0] = 1 and b[1][1] = 1 and b[1][2] = 1) or
        (b[2][0] = 1 and b[2][1] = 1 and b[2][2] = 1) or 

        #vertical wins
        (b[0][0] = 1 and b[1][0] = 1 and b[2][0] = 1) or
        (b[0][1] = 1 and b[1][1] = 1 and b[2][1] = 1) or
        (b[0][2] = 1 and b[1][2] = 1 and b[2][2] = 1) or

        #diagonal wins
        (b[0][0] = 1 and b[1][1] = 1 and b[2][2] = 1) or
        (b[0][2] = 1 and b[1][1] = 1 and b[2][0] = 1)
        #first number ([0]) = row, second number ([1]) = column
        )

def get_text(i, j, gb, l1, l2):
    pass

def isfree(i, j):
    pass

def isfull():
    pass

def gameboardplayer(game_board, l1, l2):
    pass

