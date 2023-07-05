from os import kill
import time
import pygame
import math
import socket
import json
#shrihari kulkarni 21BBS0084 from vit, vellore abhinavkondas husband was here
#############################
client_socket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',5555)
#############################
HEIGHT = 800
WIDTH = 800
pygame.init()


GameDisplay = pygame.display.set_mode((800,800))

#############INITIAL BOARD DRAWING######################
WHITE = (255,255,255)
BLACK = (165,42,42)
CHECK_HIGHLIGHT = (255,0,0)
HIGHLIGHT = (255,255,0)

game_over = [False]
white_in_check = False
black_in_check = False
white_king_moves=0
black_king_moves=0
left_wr_moves=0
right_wr_moves=0
left_br_moves=0
right_br_moves=0
square_size = 80
check = [False]
highlight = [False]
GameDisplay.fill(WHITE)

pygame.display.set_caption('CHESS')

black_rook_img=pygame.image.load('pieces/black_rook.png')
black_rook_img=pygame.transform.scale(black_rook_img,(80,80))
#GameDisplay.blit(black_rook_img,(HEIGHT/10,WIDTH/10))
#GameDisplay.blit(black_rook_img,(8*HEIGHT/10,WIDTH/10))
black_knight_img=pygame.image.load('pieces/black_knight.png')
black_knight_img=pygame.transform.scale(black_knight_img,(80,80))
#GameDisplay.blit(black_knight_img,(2*HEIGHT/10,WIDTH/10))
#GameDisplay.blit(black_knight_img,(7*HEIGHT/10,WIDTH/10))
black_bishop_img=pygame.image.load('pieces/black_bishop.png')
black_bishop_img=pygame.transform.scale(black_bishop_img,(80,80))
#GameDisplay.blit(black_bishop_img,(3*HEIGHT/10,WIDTH/10))
#GameDisplay.blit(black_bishop_img,(6*HEIGHT/10,WIDTH/10))
black_king_img=pygame.image.load('pieces/black_king.png')
black_king_img=pygame.transform.scale(black_king_img,(80,80))
#GameDisplay.blit(black_king_img,(5*HEIGHT/10,WIDTH/10))
black_queen_img=pygame.image.load('pieces/black_queen.png')
black_queen_img=pygame.transform.scale(black_queen_img,(80,80))
#GameDisplay.blit(black_queen_img,(4*HEIGHT/10,WIDTH/10))

black_pawn_img=pygame.image.load('pieces/black_pawn.png')
black_pawn_img=pygame.transform.scale(black_pawn_img,(80,80))
#GameDisplay.blit(black_pawn_img,(i*HEIGHT/10,2*WIDTH/10))
white_rook_img=pygame.image.load('pieces/white_rook.png')
white_rook_img=pygame.transform.scale(white_rook_img,(80,80))
#GameDisplay.blit(white_rook_img,(HEIGHT/10,8*WIDTH/10))
#GameDisplay.blit(white_rook_img,(8*HEIGHT/10,8*WIDTH/10))
white_knight_img=pygame.image.load('pieces/white_knight.png')
white_knight_img=pygame.transform.scale(white_knight_img,(80,80))
#GameDisplay.blit(white_knight_img,(2*HEIGHT/10,8*WIDTH/10))
#GameDisplay.blit(white_knight_img,(7*HEIGHT/10,8*WIDTH/10))
white_bishop_img=pygame.image.load('pieces/white_bishop.png')
white_bishop_img=pygame.transform.scale(white_bishop_img,(80,80))
#GameDisplay.blit(white_bishop_img,(3*HEIGHT/10,8*WIDTH/10))
#GameDisplay.blit(white_bishop_img,(6*HEIGHT/10,8*WIDTH/10))
white_king_img=pygame.image.load('pieces/white_king.png')
white_king_img=pygame.transform.scale(white_king_img,(80,80))
#GameDisplay.blit(white_king_img,(5*HEIGHT/10,8*WIDTH/10))
white_queen_img=pygame.image.load('pieces/white_queen.png')
white_queen_img=pygame.transform.scale(white_queen_img,(80,80))
#GameDisplay.blit(white_queen_img,(4*HEIGHT/10,8*WIDTH/10))

white_pawn_img=pygame.image.load('pieces/white_pawn.png')
white_pawn_img=pygame.transform.scale(white_pawn_img,(80,80))
#GameDisplay.blit(white_pawn_img,(i*HEIGHT/10,7*WIDTH/10))



Clock = pygame.time.Clock()

#black_pawn      #white_pawn 
#black_knight    #white_knight 
#black_bishop    #white_bishop 
#black_rook      #white_rook 
#black_queen     #white_queen 
#black_king      #white_king 

black_pawns = ['bp1','bp2','bp3','bp4','bp5','bp6','bp7','bp8']
white_pawns = ['wp1','wp2','wp3','wp4','wp5','wp6','wp7','wp8']

board = []
for i in range(8):
    board.append([' ',' ',' ',' ',' ',' ',' ',' '])
for i in range(8):
    board[1][i] = black_pawns[i]
    board[6][i] = white_pawns[i]

board[0] = ['br1','bkn1','bb1','bq','bk','bb2','bkn2','br2']
board[7] = ['wr1','wkn1','wb1','wq','wk','wb2','wkn2','wr2']

def Board():
    GameDisplay .fill(WHITE)
    k=0
    for i in range(1,9):
        for j in range(1,9):
            if k%2 == 0:
                pygame.draw.rect(GameDisplay,WHITE,(j*square_size,i*square_size,square_size,square_size))
            else:
                pygame.draw.rect(GameDisplay,BLACK,(j*square_size,i*square_size,square_size,square_size))
            k+=1
        k-=1
    if check[0]:
        x = check[1]    
        y = check[2]
        king = check[3]
        pygame.draw.rect(GameDisplay,CHECK_HIGHLIGHT,((y+1)*square_size,(x+1)*square_size,square_size,square_size))
        for i in board:
            if king in i:
                pygame.draw.rect(GameDisplay,CHECK_HIGHLIGHT,((i.index(king)+1)*square_size,(board.index(i)+1)*square_size,square_size,square_size))
    
    if highlight[0]:
        x = highlight[1]
        y = highlight[2]
        pygame.draw.rect(GameDisplay,HIGHLIGHT,((y+1)*square_size,(x+1)*square_size,square_size,square_size))

    for i in range(8):
        for j in range(8):
            if board[i][j][:2] == 'br':
                GameDisplay.blit(black_rook_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))
            elif board[i][j][:2] == 'wr':
                GameDisplay.blit(white_rook_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))

            elif board[i][j][:3] == 'bkn':
                GameDisplay.blit(black_knight_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))
            elif board[i][j][:3] == 'wkn':
                GameDisplay.blit(white_knight_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))
            
            elif board[i][j][:2] == 'bb':
                GameDisplay.blit(black_bishop_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))
            elif board[i][j][:2] == 'wb':
                GameDisplay.blit(white_bishop_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))
            
            elif board[i][j][:2] == 'bq':
                GameDisplay.blit(black_queen_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))
            elif board[i][j][:2] == 'wq':
                GameDisplay.blit(white_queen_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))
            
            elif board[i][j][:2] == 'bk':
                GameDisplay.blit(black_king_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))
            elif board[i][j][:2] == 'wk':
                GameDisplay.blit(white_king_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))
            
            elif board[i][j][:2] == 'bp':
                GameDisplay.blit(black_pawn_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))   
            elif board[i][j][:2] == 'wp':
                GameDisplay.blit(white_pawn_img,((j+1)*HEIGHT/10,(i+1)*WIDTH/10))

def blackBoard():
    for i in range(8):
        board[1][i] = white_pawns[i]
        board[6][i] = black_pawns[i]

    board[7] = ['br1','bkn1','bb1','bq','bk','bb2','bkn2','br2']
    board[0] = ['wr1','wkn1','wb1','wq','wk','wb2','wkn2','wr2']


def IsEmpty(initial_x,initial_y,final_x,final_y):
        global path,path_pos
        path = []
        path_pos = []
        piece = board[initial_x][initial_y][1:]
        valid = True
        def horizontal_right(ix,iy,fx,fy):
            #ix=fx,iy<fy
            for y in range(iy+1,fy+1):
                path.append(board[ix][y])
                path_pos.append([ix,y])
            return path
        def horizontal_left(ix,iy,fx,fy):
            #ix=fx,iy>fy
            for y in range(iy-1,fy-1,-1):
                path.append(board[ix][y])
                path_pos.append([ix,y])
            return path
        def vertical_up(ix,iy,fx,fy):
            #ix>fx,iy=fy
            for x in range(ix-1,fx-1,-1):
                path.append(board[x][iy])
                path_pos.append([x,iy])
            return path
        def vertical_down(ix,iy,fx,fy):
            #ix<fx,iy=fy
            for x in range(ix+1,fx+1):
                path.append(board[x][iy])
                path_pos.append([x,iy])
            return path
        def diagonal_upright(ix,iy,fx,fy):
            #ix>fx,iy<fy
            x = ix
            x-=1
            for y in range(iy+1,fy+1):
                path.append(board[x][y])
                path_pos.append([x,y])
                x-=1
            return path
        def diagonal_upleft(ix,iy,fx,fy):
            #ix>fx,iy>fy
            x = ix
            x-=1
            for y in range(iy-1,fy-1,-1):
                path.append(board[x][y])
                path_pos.append([x,y])
                x-=1
            return path
        def diagonal_downright(ix,iy,fx,fy):
            #ix<fx,iy<fy
            x=ix
            x+=1
            for y in range(iy+1,fy+1):
                path.append(board[x][y])
                path_pos.append([x,y])
                x+=1
            return path
        def diagonal_downleft(ix,iy,fx,fy):
            #ix<fx,iy>fy
            x = ix
            x+=1
            for y in range(iy-1,fy-1,-1):
                path.append(board[x][y])
                path_pos.append([x,y])
                x+=1
            return path
        
        if piece == 'kn':
            return True

        if piece == 'p':
            if initial_x < final_x:
                for i in range(initial_x+1,final_x+1):
                    path.append(board[i][initial_y])
                    path_pos.append(i,initial_y)
            else:
                
                for i in range(initial_x-1,final_x-1,-1):
                    path.append(board[i][initial_y])
                    path_pos.append(i,initial_y)

            for i in path:
                if i != ' ':
                    valid = False
        
        elif piece == 'r1' or piece == 'r2':
            if initial_x == final_x:
                if initial_y < final_y:
                    for i in horizontal_right(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
                elif initial_y > final_y:
                    for i in horizontal_left(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
            elif initial_y == final_y:
                if initial_x < final_x:
                    for i in vertical_down(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
                elif initial_x > final_x:
                    for i in vertical_up(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False

        elif piece == 'b1' or piece == 'b2':
            #up
            if initial_x > final_x:
                #left
                if initial_y > final_y:
                    for i in diagonal_upleft(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
                #right
                elif initial_y < final_y:
                    for i in diagonal_upright(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
            #down
            elif initial_x < final_x:
                #left
                if initial_y > final_y:
                    for i in diagonal_downleft(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
                #right
                elif initial_y < final_y:
                    for i in diagonal_downright(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
        elif piece == 'q' or 'k':
            #horizontal
            if initial_x == final_x:
                #right
                if initial_y < final_y:
                    for i in horizontal_right(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
                elif initial_y > final_y:
                    #left
                    for i in horizontal_left(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
            elif initial_y == final_y:
                #down
                if initial_x < final_x:
                    for i in vertical_down(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
                #up
                elif initial_x > final_x:
                    for i in vertical_up(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False

            #up
            elif initial_x > final_x:
                #left
                if initial_y > final_y:
                    for i in diagonal_upleft(initial_x,initial_y,final_x,final_y):
                        if i!= ' ':
                            valid = False
                #right
                elif initial_y < final_y:
                    for i in diagonal_upright(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
            #down
            elif initial_x < final_x:
                #left
                if initial_y > final_y:
                    for i in diagonal_downleft(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
                #right
                elif initial_y < final_y:
                    for i in diagonal_downright(initial_x,initial_y,final_x,final_y):
                        if i != ' ':
                            valid = False
        return valid
def has_white_king_moved():
    global white_king_moves
    if(board[7][4]!="wk"):
        white_king_moves=white_king_moves+1
    if(white_king_moves!=0):
        return True
    else:
        return False
def has_black_king_moved():
    global black_king_moves
    if(board[0][4]!="bk"):
        black_king_moves=black_king_moves+1
    if(black_king_moves!=0):
        return True
    else:
        return False
def has_left_wr_moved():
    global left_wr_moves
    if(board[7][0]!="wr1"):
        left_wr_moves=left_wr_moves+1
    if(left_wr_moves!=0):
        return True
    else:
        return False
def has_right_wr_moved():
    global right_wr_moves
    if(board[7][7]!="wr2"):
        right_wr_moves=right_wr_moves+1
    if(right_wr_moves!=0):
        return True
    else:
        return False
def has_left_br_moved():
    global left_br_moves
    if(board[0][0]!="br1"):
        left_br_moves=left_br_moves+1
    if(left_br_moves!=0):
        return True
    else:
        return False
def has_right_br_moved():
    global right_br_moves
    if(board[0][7]!="br2"):
        right_br_moves=right_br_moves+1
    if(right_br_moves!=0):
        return True
    else:
        return False   
    
def white_castle_left():
    global turns
    board[7][2]="wk"
    board[7][3]="wr1"
    board[7][4]=' '
    board[7][0]=' '
    Board()
    turns+=1

def white_castle_right():
    global turns
    board[7][6]="wk"
    board[7][5]="wr2"
    board[7][4]=' ' 
    board[7][7]=' '
    Board()
    turns+=1

def black_castle_left():
    global turns
    board[0][2]="bk"
    board[0][3]="br1"
    board[0][4]=" "
    board[0][0]=" "
    Board()
    turns+=1

def black_castle_right():
    global turns
    board[0][6]="bk"
    board[0][5]="br2"
    board[0][4]=" "
    board[0][7]=" "
    Board()
    turns+=1


def move(initial_coords,final_coords):
    global turns
    initial_x = initial_coords[0]
    initial_y = initial_coords[1]
    final_x = final_coords[0]
    final_y = final_coords[1]

    def capture_possibility(initial_x,initial_y,final_x,final_y):
        possible=False
        count=0
        if(IsEmpty(initial_x,initial_y,final_x,final_y)==False):
            for i in range(0,len(path)-1):
                if path[i]!=' ':
                    count+=1
            if(count==0) and(path[len(path)-1]!=' '):
                possible=True
        return possible
    
    def white_captures(initial_x,initial_y,final_x,final_y):
        global turns
        black_captured_pieces=[]
        black_captured_pieces.append(board[final_x][final_y])
        board[final_x][final_y]=' '
        board[final_x][final_y]=board[initial_x][initial_y]
        board[initial_x][initial_y]=' ' 
        Board()
    def black_captures(initial_x,initial_y,final_x,final_y):
        white_captured_pieces=[]
        white_captured_pieces.append(board[final_x][final_y])
        board[final_x][final_y]=' '
        board[final_x][final_y]=board[initial_x][initial_y]
        board[initial_x][initial_y]=' '
        Board()
    if((board[initial_x][initial_y][:2]=='wp')and(initial_x-final_x==1)and((math.fabs(initial_y-final_y))==1)and(board[final_x][final_y]!='bk')):
        if board[final_x][final_y]!=' ':
            white_captures(initial_x,initial_y,final_x,final_y)
            return True
    elif((board[initial_x][initial_y][:2]=='bp')and(initial_x-final_x==-1)and((math.fabs(initial_y-final_y))==1)and(board[final_x][final_y]!='wk')):
        if board[final_x][final_y]!=' ':
            black_captures(initial_x,initial_y,final_x,final_y)
            return True
    elif((board[initial_x][initial_y][:3]=='wkn')and(math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==2)or(math.fabs(final_x-initial_x)==2 and math.fabs(final_y-initial_y)==1)and(board[final_x][final_y]!='bk')):
        if board[final_x][final_y]!=' ':
            white_captures(initial_x,initial_y,final_x,final_y)
            return True
    elif((board[initial_x][initial_y][:2]=='bk')and(len(board[initial_x][initial_y])==4)and(math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==2)or(math.fabs(final_x-initial_x)==2 and math.fabs(final_y-initial_y)==1)and(board[final_x][final_y]!='wk')):
        if board[final_x][final_y]!=' ':
            black_captures(initial_x,initial_y,final_x,final_y)
            return True
    elif((capture_possibility(initial_x,initial_y,final_x,final_y))and(board[initial_x][initial_y][:2]=='wb')and(math.fabs(final_x-initial_x)==math.fabs(final_y-initial_y)and(board[final_x][final_y]!='bk'))):
        if board[final_x][final_y]!=' ':
            white_captures(initial_x,initial_y,final_x,final_y)
            return True
    elif((capture_possibility(initial_x,initial_y,final_x,final_y))and(board[initial_x][initial_y][:2]=='bb')and(math.fabs(final_x-initial_x)==math.fabs(final_y-initial_y)and(board[final_x][final_y]!='wk'))):
        if board[final_x][final_y]!=' ':
            black_captures(initial_x,initial_y,final_x,final_y)
            return True
    elif((capture_possibility(initial_x,initial_y,final_x,final_y))and(board[initial_x][initial_y][:2]=='wr')and((initial_x==final_x)or(initial_y==final_y))and(board[final_x][final_y]!='bk')):
        if board[final_x][final_y]!=' ':
            white_captures(initial_x,initial_y,final_x,final_y)
            return True
    elif((capture_possibility(initial_x,initial_y,final_x,final_y))and(board[initial_x][initial_y][:2]=='br')and((initial_x==final_x) or (initial_y==final_y))and(board[final_x][final_y]!='wk')):
        if board[final_x][final_y]!=' ':
            black_captures(initial_x,initial_y,final_x,final_y)
            return True
    elif((capture_possibility(initial_x,initial_y,final_x,final_y))and(board[initial_x][initial_y]=='wq')and(((initial_x==final_x) or (initial_y==final_y)) or ((math.fabs(final_x-initial_x)==math.fabs(final_y-initial_y))))and(board[final_x][final_y]!='bk')):
        if board[final_x][final_y]!=' ':
            white_captures(initial_x,initial_y,final_x,final_y)
            return True
    elif((capture_possibility(initial_x,initial_y,final_x,final_y))and(board[initial_x][initial_y]=='bq')and(((initial_x==final_x) or (initial_y==final_y)) or ((math.fabs(final_x-initial_x)==math.fabs(final_y-initial_y))))and(board[final_x][final_y]!='wk')):
        if board[final_x][final_y]!=' ':
            black_captures(initial_x,initial_y,final_x,final_y)
            return True
    elif((capture_possibility(initial_x,initial_y,final_x,final_y))and(board[initial_x][initial_y]=='wk')and(((math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==1)or(math.fabs(final_x-initial_x)==0 and math.fabs(final_y-initial_y)==1)or(math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==0)))and(board[final_x][final_y]!='bk')):
        if board[final_x][final_y]!=' ':
            fake_board = [i[:] for i in board]
            fake_board[final_x][final_y] = fake_board[initial_x][initial_y]
            fake_board[initial_x][initial_y] = ' '
            if Check(fake_board,MovingPiece):
                return False
            else:
                white_captures(initial_x,initial_y,final_x,final_y)
                return True
                
    elif((capture_possibility(initial_x,initial_y,final_x,final_y))and(board[initial_x][initial_y]=='bk')and(((math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==1)or(math.fabs(final_x-initial_x)==0 and math.fabs(final_y-initial_y)==1)or(math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==0)))and(board[final_x][final_y]!='wk')):
        if board[final_x][final_y]!=' ':
            fake_board = [i[:] for i in board]
            fake_board[final_x][final_y] = fake_board[initial_x][initial_y]
            fake_board[initial_x][initial_y] = ' '
            if Check(fake_board,MovingPiece):
                return False
            else:
                black_captures(initial_x,initial_y,final_x,final_y)
                return True
    
    ###
    def movement(initial_x,initial_y,final_x,final_y):
        global turns

        board[final_x][final_y] = MovingPiece
        board[initial_x][initial_y] = ' '
        Board()
        turns+=1

    def white_pawn_first_move(initial_x,initial_y,final_x,final_y):
        if (initial_y==final_y and ((final_x-initial_x)==-1 or (final_x-initial_x)==-2)):
            if IsEmpty(initial_x, initial_y, final_x, final_y):
                movement(initial_x,initial_y,final_x,final_y)
    
    def white_pawn_move(initial_x,initial_y,final_x,final_y):
        if (initial_y==final_y) and (final_x-initial_x==-1):
            if IsEmpty(initial_x, initial_y, final_x, final_y):
                movement(initial_x,initial_y,final_x,final_y)
    
    def black_pawn_first_move(initial_x,initial_y,final_x,final_y):
        if initial_y==final_y and ((final_x-initial_x)==1 or (final_x-initial_x)==2):
            if IsEmpty(initial_x, initial_y, final_x, final_y):
                movement(initial_x,initial_y,final_x,final_y)
    
    def black_pawn_move(initial_x,initial_y,final_x,final_y):
        if (initial_y==final_y) and (final_x-initial_x==1):
            if IsEmpty(initial_x, initial_y, final_x, final_y):
                movement(initial_x,initial_y,final_x,final_y)

    def knight_move(initial_x,initial_y,final_x,final_y):
        if (math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==2)or(math.fabs(final_x-initial_x)==2 and math.fabs(final_y-initial_y)==1):
            movement(initial_x,initial_y,final_x,final_y)

    def bishop_move(initial_x,initial_y,final_x,final_y):
        if (math.fabs(final_x-initial_x)==math.fabs(final_y-initial_y)):
            if IsEmpty(initial_x, initial_y, final_x, final_y):
                movement(initial_x,initial_y,final_x,final_y)

    def rook_move(initial_x,initial_y,final_x,final_y):
        if (initial_x==final_x) or (initial_y==final_y):
            if IsEmpty(initial_x, initial_y, final_x, final_y):
                movement(initial_x,initial_y,final_x,final_y)

    def queen_move(initial_x,initial_y,final_x,final_y):
        if ((initial_x==final_x) or (initial_y==final_y)) or ((math.fabs(final_x-initial_x)==math.fabs(final_y-initial_y))):
            if IsEmpty(initial_x, initial_y, final_x, final_y):
                movement(initial_x,initial_y,final_x,final_y)

    def king_move(initial_x,initial_y,final_x,final_y):
        if((math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==1) or (math.fabs(final_x-initial_x)==0 and math.fabs(final_y-initial_y)==1) or (math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==0)):
            if IsEmpty(initial_x, initial_y, final_x, final_y):
                movement(initial_x,initial_y,final_x,final_y)
    #if pawn first move
    if board[initial_x][initial_y][0] == 'w' and board[initial_x][initial_y][1] == 'p' and initial_x==6:
        white_pawn_first_move(initial_x,initial_y,final_x,final_y)
    
    elif board[initial_x][initial_y][0] == 'b' and board[initial_x][initial_y][1] == 'p'and initial_x==1:
        black_pawn_first_move(initial_x,initial_y,final_x,final_y)
    
    elif board[initial_x][initial_y][0] == 'w' and board[initial_x][initial_y][1] == 'p':
        white_pawn_move(initial_x,initial_y,final_x,final_y)
    
    elif board[initial_x][initial_y][0] == 'b' and board[initial_x][initial_y][1] == 'p':
        black_pawn_move(initial_x,initial_y,final_x,final_y)
    
    elif board[initial_x][initial_y][1] == 'r':
        rook_move(initial_x,initial_y,final_x,final_y)

    elif board[initial_x][initial_y][1]== 'k'and len(board[initial_x][initial_y])==4:
        knight_move(initial_x,initial_y,final_x,final_y)

    elif board[initial_x][initial_y][1] == 'b':
        bishop_move(initial_x,initial_y,final_x,final_y)

    elif board[initial_x][initial_y][1:] == 'q':
        queen_move(initial_x,initial_y,final_x,final_y)
    
    elif board[initial_x][initial_y][1] == 'k'and len(board[initial_x][initial_y])==2:
        king_move(initial_x,initial_y,final_x,final_y)
    #whitecastling
    if board[initial_x][initial_y]=="wk" and final_x==7 and final_y==2 and has_white_king_moved()==False and has_left_wr_moved()==False and board[7][1]==' ' and board[7][2]==' ' and board[7][3]==' ':
        white_castle_left()
        #return
    if board[initial_x][initial_y]=="wk" and final_x==7 and final_y==6 :
        if has_white_king_moved()==False and has_right_wr_moved()==False and board[7][5]==' ' and board[7][6]==' ':
            white_castle_right()
            #return
    #blackcastling
    if board[initial_x][initial_y]=="bk"and board[final_x][final_y]==board[0][2] and has_black_king_moved()==False and has_left_br_moved()==False and board[0][1]==" "and board[0][2]==" "and board[0][3]==" ":
        black_castle_left()
        #return
    if board[initial_x][initial_y]=="bk"and board[final_x][final_y]==board[0][6] and has_black_king_moved()==False and has_right_br_moved()==False and board[0][5]==" "and board[0][6]==" ":
        black_castle_right()
        #return
    
    
    

def Check(board,MovingPiece):
    for i in board:
        if 'bk' in i:
            black_kingx = board.index(i)
            black_kingy = i.index('bk')
        elif 'wk' in i:
            white_kingx = board.index(i)
            white_kingy = i.index('wk')
    white_king = [white_kingx,white_kingy]
    black_king = [black_kingx,black_kingy]
    
    def pawn_check():
        #diagonal down right (black)
        if black_kingx<7 and black_kingy<7 and board[black_kingx+1][black_kingy+1][:2] == 'wp':
            return 'black'
        #diagonal down left (black)
        elif black_kingx<7 and black_kingy>0 and board[black_kingx+1][black_kingy-1][:2] == 'wp':
            return 'black'
        #diagonal up right (white)
        elif white_kingx>0 and white_kingy<7 and board[white_kingx-1][white_kingy+1][:2] == 'bp':
            return 'white'
        #diagonal up left (black)
        elif white_kingx>0 and white_kingy>0 and board[white_kingx-1][white_kingy-1][:2] == 'bp':
            return 'white'
        else:
            return False
    
    def knight_check():
        def side(x,y,enemy):
            if x+2 < 8 and y+1 < 8:
                if board[x+2][y+1][:3] == enemy:
                    return True
            if x+2 < 8 and y-1 >= 0:
                if board[x+2][y-1][:3] == enemy:
                    return True
            if x+1 < 8 and y+2 < 8:
                if board[x+1][y+2][:3] == enemy:
                    return True
            if  x+1 < 8 and y-2 >= 0:
                if board[x+1][y-2][:3] == enemy:
                    return True
            if x-2 >= 0 and y+1 < 8:
                if board[x-2][y+1][:3] == enemy:
                    return True
            if x-2 >= 0 and y-1 < 8:
                if board[x-2][y-1][:3] == enemy:
                    return True
            if x-1 >= 0 and y+2 < 8:
                if board[x-1][y+2][:3] == enemy:
                    return True
            if x-1 >= 0 and y-2 >= 0:
                if board[x-1][y-2][:3] == enemy:
                    return True
        
        if side(black_kingx,black_kingy,'wkn'):
            return 'black'
        elif side(white_kingx,white_kingy,'bkn'):
            return 'white'
        else:
            return False
    
    def bishop_check():
        def side(x,y,enemy):
            k = 0
            i,j = x,y
            while (i<8 and j<8) or k==1:
                if board[i][j] == 'bk' or board[i][j] == 'wk':
                    i+=1
                    j+=1
                elif board[i][j] == ' ':
                    i+=1
                    j+=1
                elif board[i][j][:2] == enemy:
                    k = 1
                    return True
                else:
                    break
            i,j = x,y
            while (i>=0 and j>=0) or k==1:
                if board[i][j] == 'bk' or board[i][j] == 'wk':
                    i-=1
                    j-=1
                elif board[i][j] == ' ':
                    i-=1
                    j-=1
                elif board[i][j][:2] == enemy:
                    k = 1
                    return True
                else:
                    break
            i,j = x,y
            while (i<8 and j>=0) or k==1:
                if board[i][j] == 'bk' or board[i][j] == 'wk':
                    i+=1
                    j-=1
                elif board[i][j] == ' ':
                    i+=1
                    j-=1
                elif board[i][j][:2] == enemy:
                    k = 1
                    return True
                else:
                    break
            i,j = x,y
            while(i>=0 and j<8) or k==1:
                if board[i][j] == 'bk' or board[i][j] == 'wk':
                    i-=1
                    j+=1
                elif board[i][j] == ' ':
                    i-=1
                    j+=1
                elif board[i][j][:2] == enemy:
                    k = 1
                    return True
                else:
                    break
            return False
        

        if side(white_kingx,white_kingy,'bb'):
            return 'white'
        elif side(black_kingx,black_kingy,'wb'):
            return 'black'
        elif side(white_kingx,white_kingy,'bq'):
            return 'white'
        elif side(black_kingx,black_kingy,'wq'):
            return 'black'
        else:
            return False

    def rook_check():
        def side(x,y,enemy):
            i,j = x,y 
            k = 0
            while i<8 or k==1:
                if board[i][j]=='bk' or board[i][j]=='wk':
                    i+=1
                elif board[i][j] == ' ':
                    i+=1
                elif board[i][j][:2] == enemy:
                    k = 1
                    return True
                else:
                    break
            i,j = x,y
            while j<8 or k==1:
                if board[i][j] == ' ' or board[i][j]=='bk' or board[i][j]=='wk':
                    j+=1
                elif board[i][j][:2] == enemy:
                    k = 1
                    return True
                else:
                    break
            i,j = x,y
            while i>=0 or k==1:
                if board[i][j] == ' ' or board[i][j]=='bk' or board[i][j]=='wk':
                    i-=1
                elif board[i][j][:2] == enemy:
                    k = 1
                    return True
                else:
                    break
            i,j = x,y
            while j>=0 or k==1:
                if board[i][j] == ' ' or board[i][j]=='bk' or board[i][j]=='wk':
                    j-=1
                elif board[i][j][:2] == enemy:
                    k = 1
                    return True
                else:
                    break
            return False

        if side(white_kingx,white_kingy,'br'):
            return 'white'
        elif side(black_kingx,black_kingy,'wr'):
            return 'black'
        elif side(white_kingx,white_kingy,'bq'):
            return 'white'
        elif side(black_kingx,black_kingy,'wq'):
            return 'black'
        else:
            return False
        
    if pawn_check():
        return pawn_check()
    elif knight_check():
        return knight_check()
    elif bishop_check():
        return bishop_check()
    elif rook_check():
        return rook_check() 
    else:
        return False
    

def CheckMate(board,MovingPiece,king):
    #conditions for checkmate:
    #if king can't get out
    #if checking piece can't be blocked
    #if checking piece can't be captured
    for i in board:
        if king in i:
            kingx = board.index(i)
            kingy = i.index(king)
            checkedKing = [kingx,kingy]
        if MovingPiece in i:
            enemyx = board.index(i)
            enemyy = i.index(MovingPiece)

    def checkEscape():
        #king has 8 possible moves
        #up
        fake_board = [i[:] for i in board]
        if kingx>0 and fake_board[kingx-1][kingy]==' ': 
            fake_board[kingx-1][kingy] = fake_board[kingx][kingy]
            fake_board[kingx][kingy] = ' '
            print('1')
            if Check(fake_board,MovingPiece) == False:
                return True
        #down
        fake_board = [i[:] for i in board]
        if kingx<7 and fake_board[kingx+1][kingy]==' ':
            fake_board[kingx+1][kingy] = fake_board[kingx][kingy]
            fake_board[kingx][kingy] = ' '
            print('2')
            if Check(fake_board,MovingPiece) == False:
                return True
        #left
        fake_board = [i[:] for i in board]
        if kingy>0 and fake_board[kingx][kingy-1]==' ':
            fake_board[kingx][kingy-1] = fake_board[kingx][kingy]
            fake_board[kingx][kingy] = ' '
            print('3')
            if Check(fake_board,MovingPiece) == False:
                return True
        #right
        fake_board = [i[:] for i in board]
        if kingy<7 and fake_board[kingx][kingy+1]==' ':
            fake_board[kingx][kingy+1] = fake_board[kingx][kingy]
            fake_board[kingx][kingy] = ' '
            print('4')
            for i in fake_board:
                print(i)
            print('\n')
            if Check(fake_board,MovingPiece) == False:
                return True
        #upleft
        fake_board = [i[:] for i in board]
        if kingx>0 and kingy>0 and fake_board[kingx-1][kingy-1]==' ':
            fake_board[kingx-1][kingy-1] = fake_board[kingx][kingy]
            fake_board[kingx][kingy] = ' '
            print('5')
            if Check(fake_board,MovingPiece) == False:
                return True
        #upright
        fake_board = [i[:] for i in board]
        if kingx>0 and kingy<7 and fake_board[kingx-1][kingy+1]==' ':
            fake_board[kingx-1][kingy+1] = fake_board[kingx][kingy]
            fake_board[kingx][kingy] = ' '
            print('6')
            if Check(fake_board,MovingPiece) == False:
                return True
        #downleft
        fake_board = [i[:] for i in board]
        if kingx<7 and kingy>0 and fake_board[kingx+1][kingy-1]==' ':
            fake_board[kingx+1][kingy-1] = fake_board[kingx][kingy]
            fake_board[kingx][kingy] = ' '
            print('7')
            if Check(fake_board,MovingPiece) == False:
                return True
        #downright
        fake_board = [i[:] for i in board]
        if kingx<7 and kingy<7 and fake_board[kingx+1][kingy+1]==' ':
            fake_board[kingx+1][kingy+1] = fake_board[kingx][kingy]
            fake_board[kingx][kingy] = ' '
            print('8')
            if Check(fake_board,MovingPiece) == False:
                return True     
        return False
        
            
    def checkBlock():
        checkTake = False
        IsEmpty(kingx,kingy,enemyx,enemyy) #this is just to get the path variable from enemy to king

        def blockable(x,y,checkTake=False):
            temp_x = x
            temp_y = y
            if king == 'wk':
                team = ['wp','wkn','wb','wr','wq','wk']
            else:
                team = ['bp','bkn','bb','br','bq','bk']
        
            #pawns
            if checkTake == False:
                #pawn
                if king == 'wk':
                    if (x+1)<8 and board[x+1][y][:2] == team[0]:
                        if IsEmpty(x+1,y,x,y):
                            print('1')
                            return True

                    if (x+2)<8 and board[x+2][y][:2]==team[0] and (x+2)==6:
                        if IsEmpty(x+2,y,x,y):
                            print('2')
                            return True
                else:
                    if (x-1)>=0 and board[x-1][y][:2] == team[0]:
                        if IsEmpty(x-1,y,x,y):
                            print('1')
                            return True
                    if (x-2)>=0 and board[x-2][y][:2]==team[0] and (x-2)==1:
                        if IsEmpty(x-2,y,x,y):
                            print('2')
                            return True
            else:
                if king == 'wk':
                    if (x+1)<8 and (y-1)>=0 and board[x+1][y-1][:2] == team[0]:
                        return True
                    if (x+1)<8 and (y+1)<8 and board[x+1][y+1][:2] == team[0]:
                        return True
                else:
                    if (x-1)>=0 and (y-1)>=0 and board[x-1][y-1][:2] == team[0]:
                        return True
                    if (x-1)>=0 and (y+1)<8 and board[x-1][y+1][:2] == team[0]:
                        return True

            #knights
            #-upleft
            if (x-1)>=0 and (y-2)>=0 and board[x-1][y-2][:3] == team[1]:
                if IsEmpty(x-1,y-2,x,y):
                    print('3')
                    return True
                if checkTake:
                    return True
            if (x-2)>=0 and (y-1)>=0 and board[x-2][y-1][:3] == team[1]:
                if IsEmpty(x-2,y-1,x,y):
                    print('4')
                    return True
                if checkTake:
                    return True
            #-upright
            if (x-1)>=0 and (y+2)<8 and board[x-1][y+2][:3] == team[1]:
                if IsEmpty(x-1,y+2,x,y):
                    print('5')
                    return True
                if checkTake:
                    return True
            if (x-2)>=0 and (y+1)<8 and board[x-2][y+1][:3] == team[1]:
                if IsEmpty(x-2,y+1,x,y):
                    print('6')
                    return True
                if checkTake:
                    return True
            #-downleft
            if (x+1)<8 and (y-2)>=0 and board[x+1][y-2][:3] == team[1]:
                if IsEmpty(x+1,y-2,x,y):
                    print('7')
                    return True
                if checkTake:
                    return True
            if (x+2)<8 and (y-1)>=0 and board[x+2][y-1][:3] == team[1]:
                if IsEmpty(x+2,y-1,x,y):
                    print('8')
                    return True
                if checkTake:
                    return True
            #-downright
            if (x+1)<8 and (y+2)<8 and board[x+1][y+2][:3] == team[1]:
                if IsEmpty(x+1,y+2,x,y):
                    print('9')
                    return True
                if checkTake:
                    return True
            if (x+2)<8 and (y+1)<8 and board[x+2][y+1][:3] == team[1]:
                if IsEmpty(x+2,y+1,x,y):
                    print('10')
                    return True
                if checkTake:
                    return True
            

            #bishops
            #-upleft
            temp_x = x
            temp_y = y
            while (temp_x-1)>=0 and (temp_y-1)>=0:
                if board[temp_x-1][temp_y-1][:2] == team[2]:
                    if IsEmpty(temp_x-1,temp_y-1,x,y):
                        print('11')
                        return True
                    if checkTake:
                        if IsEmpty(temp_x-1,temp_y-1,x+1,y+1):
                            return True
                temp_x-=1
                temp_y-=1

            #-upright
            temp_x = x
            temp_y = y
            while (temp_x-1)>=0 and (temp_y+1)<8:
                if board[temp_x-1][temp_y+1][:2] == team[2]:
                    if IsEmpty(temp_x-1,temp_y+1,x,y):
                        print('12')
                        return True
                    if checkTake:
                        if IsEmpty(temp_x-1,temp_y+1,x+1,y-1):
                            return True
                temp_x-=1
                temp_y+=1
            #-downleft
            temp_x = x
            temp_y = y
            while (temp_x+1)<8 and (temp_y-1)<8:
                if board[temp_x+1][temp_y-1][:2] == team[2]:
                    if IsEmpty(temp_x+1,temp_y-1,x,y):
                        print('13')
                        return True
                    if checkTake:
                        if IsEmpty(temp_x+1,temp_y-1,x-1,y+1):
                            return True
                temp_x+=1
                temp_y-=1
            #-downright
            temp_x = x
            temp_y = y
            while (temp_x+1)<8 and (temp_y+1)<8:
                if board[temp_x+1][temp_y+1][:2] == team[2]:
                    if IsEmpty(temp_x+1,temp_y+1,x,y):
                        print('14')
                        return True
                    if checkTake:
                        if IsEmpty(temp_x+1,temp_y+1,x-1,y-1):
                            return True
                temp_x+=1
                temp_y+=1

            else:
                pass

            #rooks
            #-up
            temp_x = x
            temp_y = y
            while (temp_x-1)>=0:
                if board[temp_x-1][temp_y][:2] in [team[3],team[4]]:
                    if IsEmpty(temp_x-1,temp_y,x,y):
                        print('15')
                        return True
                    if checkTake:
                        if IsEmpty(temp_x-1,temp_y,x+1,y):
                            return True
                temp_x-=1
            #-down
            temp_x = x
            temp_y = y
            while(temp_x+1)<8:
                if board[temp_x+1][temp_y][:2] in [team[3],team[4]]:
                    if IsEmpty(temp_x+1,temp_y,x,y):
                        print('16')
                        return True
                    if checkTake:
                        if IsEmpty(temp_x+1,temp_y,x-1,y):
                            return True
                temp_x+=1
            #-left
            temp_x = x
            temp_y = y
            while(temp_y-1>=0):
                if board[temp_x][temp_y-1][:2] in [team[3],team[4]]:
                    if IsEmpty(temp_x,temp_y-1,x,y):
                        print('17')
                        return True
                    if checkTake:
                        if IsEmpty(temp_x,temp_y-1,x,y+1):
                            return True
                temp_y-=1
            #-right
            temp_x = x
            temp_y = y
            while(temp_y+1<8):
                if board[temp_x][temp_y+1][:2] in [team[3],team[4]]:
                    if IsEmpty(temp_x,temp_y+1,x,y):
                        print('18')
                        return True
                    if checkTake:
                        if IsEmpty(temp_x,temp_y+1,x,y-1):
                            return True
                temp_y+=1
            
        for i in path_pos[:len(path_pos)-1]:
            print(i)
            if blockable(i[0],i[1]):
                return True

        
        checkTake = True
        if blockable(enemyx,enemyy,checkTake):
            return True
        else:
            return False

    #print(checkEscape())
    checkList = [checkEscape(),checkBlock()]
    print(checkList,'..checklist')
    if True not in checkList:
        return True
    else:
        return False

def displayWinner(winner):
    if winner == 'white':
        white_win_img=pygame.image.load('pieces/white_win.jpg')
        #white_win_img=pygame.transform.scale(white_win_img,(80,80))
        GameDisplay.blit(white_win_img,(HEIGHT//2,WIDTH//2))
        #displayWinner('white')
    elif winner == 'black':
        black_win_img=pygame.image.load('pieces/black_win.jpg')
        #black_win_img=pygame.transform.scale(black_win_img,(80,80))
        GameDisplay.blit(black_win_img,(HEIGHT//2,WIDTH//2))
        #displayWinner('black')


def ClickedSquare(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    x = x//80 - 1
    y = y//80 - 1
    return [y,x]

running = True
step = 0
turns = 0
Board()

try:
    client_socket.connect(server_address)

    team = client_socket.recv(4096).decode()
    print(team)
    if team == 'black':
        blackBoard()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                #print(turns)
                mouse_position = pygame.mouse.get_pos()
                clicked_coords = ClickedSquare(mouse_position)

                try:
                    item = board[clicked_coords[0]][clicked_coords[1]]
                    if clicked_coords[0] < 0 or clicked_coords[1] < 0:
                        pass
                    elif item != ' ' and step==0:
                        if (turns%2==0 and board[clicked_coords[0]][clicked_coords[1]][0] == 'w')or(turns%2==1 and board[clicked_coords[0]][clicked_coords[1]][0] == 'b'):
                            initial_coordinates = clicked_coords
                            MovingPiece = board[clicked_coords[0]][clicked_coords[1]]
                        
                            highlight = [True,clicked_coords[0],clicked_coords[1]]
                            Board()
                            highlight = [False]
                            step = 1
                    elif item !=' ' and step==1:
                        #if the piece they clicked on is of same colour as their initial click
                        MovingPiece = board[clicked_coords[0]][clicked_coords[1]]
                        if MovingPiece[0] == board[initial_coordinates[0]][initial_coordinates[1]][0]:
                            initial_coordinates = clicked_coords
                            highlight = [True,clicked_coords[0],clicked_coords[1]]
                            Board()
                            highlight = [False]
                        #this is if they try to capture a piece (click on their piece and then the enemy piece)
                        else:
                            fake_board = [i[:] for i in board]
                            killing_piece = fake_board[initial_coordinates[0]][initial_coordinates[1]]
                            fake_board[clicked_coords[0]][clicked_coords[1]] = killing_piece
                            fake_board[initial_coordinates[0]][initial_coordinates[1]] = ' '
                            for i in board:
                                print(i)
                            if Check(fake_board,killing_piece) == 'black':
                                check = [True,clicked_coords[0],clicked_coords[1],'bk']
                                print('black is under check')
                                if CheckMate(fake_board,killing_piece,'bk'):
                                    print('checkmate! White wins!3')
                                    game_over = [True,'white']
                                    
                                    white_win_img=pygame.image.load('pieces/white_win.jpg')
                                    white_win_img=pygame.transform.scale(white_win_img,(80,80))
                                    GameDisplay.blit(white_win_img,(HEIGHT//2,WIDTH//2))
                                    game_over = [True,'white']
                                    

                            elif Check(fake_board,killing_piece) == 'white':
                                check = [True,clicked_coords[0],clicked_coords[1],'wk']
                                print('white is under check')
                                for i in fake_board:
                                    print(i)
                                if CheckMate(fake_board,killing_piece,'wk'):
                                    print('checkmate! Black wins!4')
                                    game_over = [True,'black']
                                    
                            else:
                                check = [False]
                            
                            
                            print(board[initial_coordinates[0]][initial_coordinates[1]],' captures ',board[clicked_coords[0]][clicked_coords[1]])
                                
                            if Check(fake_board, MovingPiece) == 'black' and turns%2!=0:
                                print('black moving into check')
                                print('black is under check')    
                                step = 0
                            elif Check(fake_board,MovingPiece) == 'white' and turns%2==0:
                                print('white moving into check')
                                print('white is under check')
                                step = 0
                            else:
                                if move(initial_coordinates,clicked_coords):
                                    step = 0
                                    turns += 1
                            
                            move = board
                            client_socket.send(move.encode())
                            game_state = client_socket.recv(4096).decode()


                    elif item == ' ' and step == 1:
                        
                        fake_board = [i[:] for i in board]
                        fake_board[clicked_coords[0]][clicked_coords[1]] = MovingPiece
                        fake_board[initial_coordinates[0]][initial_coordinates[1]] = ' '

                        #so that team cannot move into checking itself
                        if Check(fake_board, MovingPiece) == 'black' and turns%2!=0:
                            print('black is under check')    
                            step = 0
                        elif Check(fake_board,MovingPiece) == 'white' and turns%2==0:
                            print('white is under check')
                            step = 0

                        elif Check(fake_board,MovingPiece) == 'black' and turns%2==0:
                            print('black is under check')
                            check = [True,clicked_coords[0],clicked_coords[1],'bk']
                            move(initial_coordinates,clicked_coords)
                            if CheckMate(fake_board, MovingPiece,'bk'):
                                print('checkmate! White wins!1')
                                game_over = [True,'white']
                            step = 0
                            #turns += 1
                        elif Check(fake_board,MovingPiece) == 'white' and turns%2!=0:
                            print('white is under check')
                            check = [True,clicked_coords[0],clicked_coords[1],'wk']
                            move(initial_coordinates,clicked_coords)
                            if CheckMate(fake_board, MovingPiece,'wk'):
                                print('checkmate! Black wins!2')
                                game_over = [True,'black']
                            step = 0
                            #turns += 1
                        else:
                            check = [False]
                            move(initial_coordinates,clicked_coords)

                            step = 0
                            #turns += 1
                    if game_over[0]:
                        displayWinner(game_over[1])
                except IndexError:
                    pass
                    
                #for i in board:
                #   print(i)

        
        pygame.display.update()

        # move = json.dumps(board)

        # client_socket.send(move.encode())

        # game_state = client_socket.recv(4096).decode() 

        # board = json.loads(game_state)


except socket.error as e:
    print(e)

finally:
    client_socket.close()