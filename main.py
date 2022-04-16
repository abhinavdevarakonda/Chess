import time
import pygame
import math

pygame.init()
HEIGHT=800
WIDTH=800
GameDisplay = pygame.display.set_mode((HEIGHT,WIDTH))

WHITE = (255,255,255)
BLACK = (165,42,42)
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
black_rook_img=pygame.image.load('pieces/black_rook.png')
black_rook_img=pygame.transform.scale(black_rook_img,(80,80))
GameDisplay.blit(black_rook_img,(HEIGHT/10,WIDTH/10))
GameDisplay.blit(black_rook_img,(8*HEIGHT/10,WIDTH/10))
black_knight_img=pygame.image.load('pieces/black_knight.png')
black_knight_img=pygame.transform.scale(black_knight_img,(80,80))
GameDisplay.blit(black_knight_img,(2*HEIGHT/10,WIDTH/10))
GameDisplay.blit(black_knight_img,(7*HEIGHT/10,WIDTH/10))
black_bishop_img=pygame.image.load('pieces/black_bishop.png')
black_bishop_img=pygame.transform.scale(black_bishop_img,(80,80))
GameDisplay.blit(black_bishop_img,(3*HEIGHT/10,WIDTH/10))
GameDisplay.blit(black_bishop_img,(6*HEIGHT/10,WIDTH/10))
black_king_img=pygame.image.load('pieces/black_king.png')
black_king_img=pygame.transform.scale(black_king_img,(80,80))
GameDisplay.blit(black_king_img,(4*HEIGHT/10,WIDTH/10))
black_queen_img=pygame.image.load('pieces/black_queen.png')
black_queen_img=pygame.transform.scale(black_queen_img,(80,80))
GameDisplay.blit(black_queen_img,(5*HEIGHT/10,WIDTH/10))
i=1
while i<=8:
    black_pawn_img=pygame.image.load('pieces/black_pawn.png')
    black_pawn_img=pygame.transform.scale(black_pawn_img,(80,80))
    GameDisplay.blit(black_pawn_img,(i*HEIGHT/10,2*WIDTH/10))
    i=i+1
white_rook_img=pygame.image.load('pieces/white_rook.png')
white_rook_img=pygame.transform.scale(white_rook_img,(80,80))
GameDisplay.blit(white_rook_img,(HEIGHT/10,8*WIDTH/10))
GameDisplay.blit(white_rook_img,(8*HEIGHT/10,8*WIDTH/10))
white_knight_img=pygame.image.load('pieces/white_knight.png')
white_knight_img=pygame.transform.scale(white_knight_img,(80,80))
GameDisplay.blit(white_knight_img,(2*HEIGHT/10,8*WIDTH/10))
GameDisplay.blit(white_knight_img,(7*HEIGHT/10,8*WIDTH/10))
white_bishop_img=pygame.image.load('pieces/white_bishop.png')
white_bishop_img=pygame.transform.scale(white_bishop_img,(80,80))
GameDisplay.blit(white_bishop_img,(3*HEIGHT/10,8*WIDTH/10))
GameDisplay.blit(white_bishop_img,(6*HEIGHT/10,8*WIDTH/10))
white_king_img=pygame.image.load('pieces/white_king.png')
white_king_img=pygame.transform.scale(white_king_img,(80,80))
GameDisplay.blit(white_king_img,(4*HEIGHT/10,8*WIDTH/10))
white_queen_img=pygame.image.load('pieces/white_queen.png')
white_queen_img=pygame.transform.scale(white_queen_img,(80,80))
GameDisplay.blit(white_queen_img,(5*HEIGHT/10,8*WIDTH/10))
i=1
while i<=8:
    white_pawn_img=pygame.image.load('pieces/white_pawn.png')
    white_pawn_img=pygame.transform.scale(white_pawn_img,(80,80))
    GameDisplay.blit(white_pawn_img,(i*HEIGHT/10,7*WIDTH/10))
    i=i+1



Clock = pygame.time.Clock()

#black_pawn      #white_pawn 
#black_knight    #white_knight 
#black_bishop    #white_bishop 
#black_rook      #white_rook 
#black_queen     #white_queen 
#black_king      #white_king 
class PIECE:
    def __init__(self,piece,colour,picture):
        self.piece = piece
        self.colour = colour
        self.picture = picture

black_pawn = PIECE('pawn','black','black_pawn.png')
white_pawn = PIECE('pawn','white','white_pawn.png')
black_knight = PIECE('knight','black','black_knight.png')
white_knight = PIECE('knight','white','white_knight.png')
black_bishop = PIECE('bishop','black','black_bishop')
white_bishop = PIECE('bishop','white','white_bishop.png')
black_rook = PIECE('rook','black','black_rook.png')
white_rook = PIECE('rook','white','white_rook.png')
black_queen = PIECE('queen','black','black_queen.png')
white_queen = PIECE('queen','white','white_queen.png')
black_king = PIECE('king','black','black_king.png')
white_king = PIECE('king','white','white_king.png')
empty_square = PIECE('.',' ',' ')
def Board():
    global board
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(empty_square)
    
    for i in range(8):
        board[1][i] = white_pawn
        board[7][i] = black_pawn
    
    
    board[0] = [white_rook,white_knight,white_bishop,white_king,white_queen,white_bishop,white_knight,white_rook]
    board[6] = [black_rook,black_knight,black_bishop,black_king,black_king,black_bishop,black_knight,black_rook]
    for i in range(8):
        print('\n')
        for j in range(8):
            print(board[i][j].piece,end=' ')
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
