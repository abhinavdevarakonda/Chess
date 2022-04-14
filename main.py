import time
import pygame

#black_pawn      #white_pawn 
#black_knight    #white_knight 
#black_bishop    #white_bishop 
#black_rook      #white_rook 
#black_queen     #white_queen 
#black_king      #white_king 


def Board():
    board = [8]
    for i in range(2,5):
        for j in range(8):
            board[i][j]=' '
    
    for i in range(8):
        board[1][i] = 'white_pawn'
        board[6][i] = 'black_pawn'
    
    board[0]=['white_rook','white_knight','white_bishop','white_queen','white_king','white_bishop','white_knight','white_rook']
    board[7]=['black_rook','black_knight','black_bishop','black_queen','black_king','black_bishop','black_knight','black_rook']
    print(board)
Board()


