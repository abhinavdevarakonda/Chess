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
        board[1][i] = 'bp'
        board[6][i] = 'wp'
    
    board[0] = ['br','bk','bb','bking','bqueen','bb','bk','br']
    board[7] = ['wr','wk','wb','wking','wqueen','wb','wk','wr']

    return board
Board()

