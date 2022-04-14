import time
import pygame
import math

pygame.init()
GameDisplay = pygame.display.set_mode((800,800))

WHITE = (255,255,255)
BLACK = (0,0,0)
square_size = 80
GameDisplay.fill(WHITE)

k=0
for i in range(1,9):
    for j in range(1,9):
        if k%2 == 0:
            pygame.draw.rect(GameDisplay,WHITE,(j*square_size,i*square_size,square_size,square_size))
        else:
            pygame.draw.rect(GameDisplay,BLACK,(j*square_size,i*square_size,square_size,square_size))
        k+=1
    k-=1

pygame.display.set_caption('CHESS')
Clock = pygame.time.Clock()

#black_pawn      #white_pawn 
#black_knight    #white_knight 
#black_bishop    #white_bishop 
#black_rook      #white_rook 
#black_queen     #white_queen 
#black_king      #white_king 


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
        pass


end = False
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
    pygame.display.update()
