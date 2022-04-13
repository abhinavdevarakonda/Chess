import time
import pygame

#black_pawn = bp
#black_knight = bk
#black_bishop = bb
#black_rook = br
#black_queen = bqueen
#black_king = bking

#white_pawn = wp
#white_knight = bk
#white_bishop = wb
#white_rook = wr
#white_queen = wqueen
#white_king = wking

def Board():
    board = []
    for i in range(8):
        board.append([' ',' ',' ',' ',' ',' ',' ',' '])
    
    for i in range(8):
        board[1][i] = 'bp'
        board[6][i] = 'wp'
    
    board[0] = ['br','bk','bb','bking','bqueen','bb','bk','br']
    board[7] = ['wr','wk','wb','wking','wqueen','wb','wk','wr']

    return board
Board()

