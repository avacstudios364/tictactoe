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
        (b[0][0] == l and b[0][1] == l and b[0][2] == l) or
        (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
        (b[2][0] == l and b[2][1] == l and b[2][2] == l) or 

        #vertical wins
        (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
        (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
        (b[0][2] == l and b[1][2] == l and b[2][2] == l) or

        #diagonal wins
        (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
        (b[0][2] == l and b[1][1] == l and b[2][0] == l)
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
        
        for j in range(3): # for column
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd = 5, bg = 'green', fg = 'white', 
            command = get_t, height = 8, width = 8)
            button[i][j].grid(row = m, column = n) # m = rows, n = columns
    game_board.mainloop()

#defines the next move of computer
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i],[j])
    move = []
    if possiblemove == ' ':
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return [i]
        
        corner = []
        for i in possiblemove:
            for i in [[0,0],[2,0],[0,2],[2,2]]:
                corner.append(i)
            if len(corner) > 0:
                move = random.randint(0,len(corner) - 1)
                return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0,1],[1,0],[1,2],[2,1]]:
                edge.append(i)
            if len(edge) > 0:
                move = random.randint(0,len(edge) - 1)
                return edge[move]


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
    l1 = Button(game_board, text ='Player 1: X', width = 15, bg = 'red', fg = 'white')
    l1.grid(row = 1, column = 1)
    l2 = Button(game_board, text = 'Player 2: O', width = 15, bg = 'white', fg = 'red')
    l2.grid(row = 2, column = 1)
    gameboard_player(game_board, l1, l2)


def play():
    menu = Tk()
    menu.geometry('500x500')
    menu.title('Tic Tac Toe')
    wpl = partial(withplayer, menu) #wpl = withplayer
    wpc = partial(withpc, menu) #wpc = withpc
    headbtn = Button(menu, text = 'Welcome to Tic Tac Toe', bg = 'red', fg = 'white',
                    activeforeground = 'white', activebackground = 'red', bd = 5, width = 50)
    headbtn.pack(side = 'top')
    b1 = Button(menu, text = '1 player', bg = 'yellow', fg = 'green',
                activeforeground = 'yellow', activebackground = 'green', bd = 3, command = wpc, width = 50)
    b1.pack(side = 'top')

    b2 = Button(menu, text = '2 player', bg = 'green', fg = 'yellow',
                activeforeground = 'green', activebackground = 'yellow', bd = 3, command = wpl, width = 50)
    b2.pack(side = 'top')
    bexit = Button(menu, text = 'Exit', bg = 'red', fg = 'black',
                activeforeground = 'black', activebackground = 'red', width = 300, bd = 5, command = menu.quit)
    bexit.pack(side = 'bottom')
    menu.mainloop()

if __name__ == '__main__':
    play()

def play():
    pass

if __name__ == '__main__':
    play()
