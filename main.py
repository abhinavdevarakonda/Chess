import time
import pygame

#black_pawn = bp          #white_pawn = wp
#black_knight = bk        #white_knight = bk
#black_bishop = bb        #white_bishop = wb
#black_rook = br          #white_rook = wr
#black_queen = bqueen     #white_queen = wqueen
#black_king = bking       #white_king = wking


def Board():
    board = []
    for i in range(8):
        board.append([' ',' ',' ',' ',' ',' ',' ',' '])
    
    for i in range(8):
        board[1][i] = 'wp'
        board[6][i] = 'bp'
    
    board[0] = ['wr','wk','wb','wking','wqueen','wb','wk','wr']
    board[7] = ['br','bk','bb','bking','bqueen','bb','bk','br']
    for i in range(8):
        print(board[i],"\n")
Board()
def move(initial_x,initial_y,final_x,final_y):
    board=[]
    board[final_x][final_y]=board[initial_x][initial_y]
    board[initial_x][initial_y]=' '
def white_pawn_first_move(initial_x,initial_y,final_x,final_y):
    board=[]
    if initial_x==final_x and board[initial_x][initial_y]=='wp' and (final_y-initial_y==1 or final_y-initial_y==2):
        board[final_x][final_y]=board[initial_x][initial_y]
        board[initial_x][initial_y]=' '
def black_pawn_first_move(initial_x,initial_y,final_x,final_y):
    board=[]
    if initial_x==final_x and board[initial_x][initial_y]=='bp' and (final_y-initial_y==1 or final_y-initial_y==2):
        board[final_x][final_y]=board[initial_x][initial_y]
        board[initial_x][initial_y]=' '



