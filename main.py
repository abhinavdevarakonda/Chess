import time
import pygame
import math

#black_pawn = bp          #white_pawn = wp
#black_knight = bk        #white_knight = bk
#black_bishop = bb        #white_bishop = wb
#black_rook = br          #white_rook = wr
#black_queen = bqueen     #white_queen = wqueen
#black_king = bking       #white_king = wking


def Board():
    global board
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
    board[final_x][final_y]=board[initial_x][initial_y]
    board[initial_x][initial_y]=' '
def pawn_first_move(initial_x,initial_y,final_x,final_y):
    if initial_x==final_x and (final_y-initial_y==1 or final_y-initial_y==2):
        move(initial_x,initial_y,final_x,final_y)
def knight_move(initial_x,initial_y,final_x,final_y):
    if (math.fabs(final_x-initial_x==1) and math.fabs(final_y-initial_y==2))or(math.fabs(final_x-initial_x)==2 and math.fabs(final_y-initial_y==1)):
        move(initial_x,initial_y,final_x,final_y)
def bishop_move(initial_x,initial_y,final_x,final_y):
    if (math.fabs(final_x-initial_x)==math.fabs(final_y-initial_y)):
        move(initial_x,initial_y,final_x,final_y)
def rook_move(initial_x,initial_y,final_x,final_y):
    if (initial_x==final_x) or (initial_y==final_y):
        move(initial_x,initial_y,final_x,final_y)
def queen_move(initial_x,initial_y,final_x,final_y):
    if (initial_x==final_x) or (initial_y==final_y):

