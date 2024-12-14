from tkinter import *
import random
from functools import partial
from tkinter import messagebox
from copy import deepcopy

sign = 0 #sign variable to decide what player it is the turn of
global board
board = [['' for x in range(3)] for i in range(3)]

print(board)

def winner(b,l): #b is for board and l is for player
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
    global sign 
    if board[i][j] == '':
        if sign % 2 == 0:
            l1.config(state = DISABLED)
            l2.config(state = ACTIVE)
            board[i][j] = 'X'
        else:
            l1.config(state = ACTIVE)
            l2.config(state = DISABLED)
            board[i][j] = 'O'
        sign = sign + 1
        button[i][j].config(text = board[i][j])
    if winner(board, 'X'):
        gb.destroy() #gb = gameboard
        box = messagebox.showinfo('Winner', 'Player 1 won the match')
    elif winner(board, 'O'):
        gb.destroy()
        box = messagebox.showinfo('Winner', 'Player 2 won the match')
    elif (isfull()):
        gb.destroy()
        box = messagebox.showinfo('Draw', 'Its a draw!')


def isfree(i, j):
    return board[i][j] == ' '

def isfull():
    flag = True
    for i in board:
        if(i.count('') > 0):
            flag = False
    return flag

#gui of gameboard to play with another player
def gameboard_player(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        
        for g in range(3): # for column
            n = j
            button.append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd = 5, bg = 'green', fg = 'white', 
            command = get_t, height = 8, width = 8)
            button[i][j].grid(row = m, column = n) # m = rows, n = columns
    game_board.mainloop()


def pc():
    pass

def get_text_pc(i, j, bg, l1, l2):
    pass


#gui of gameboard to play with computer
def gameboard_pc(gameboard, l1, l2):
    pass

def withpc(gameboard):
    pass

# to initualize the game with another player
def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title('Tic Tac Toe')
    l1 = Button(game_board, text ='Player 1: X', width = 15)

def play():
    pass

if __name__ == '__main__':
    play()
