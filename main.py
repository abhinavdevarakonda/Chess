import time
import pygame
import math

HEIGHT = 800
WIDTH = 800
pygame.init()

GameDisplay = pygame.display.set_mode((800,800))

#############INITIAL BOARD DRAWING######################
WHITE = (255,255,255)
BLACK = (165,42,42)
white_in_check = False
black_in_check = False
square_size = 80
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



def move(initial_coords,final_coords):
    initial_x = initial_coords[0]
    initial_y = initial_coords[1]
    final_x = final_coords[0]
    final_y = final_coords[1]

    def IsEmpty(initial_x,initial_y,final_x,final_y):
        global path
        path = []
        piece = board[initial_x][initial_y][1:]
        valid = True
        def horizontal_right(ix,iy,fx,fy):
            #ix=fx,iy<fy
            for y in range(iy+1,fy+1):
                path.append(board[ix][y])
            return path
        def horizontal_left(ix,iy,fx,fy):
            #ix=fx,iy>fy
            for y in range(iy-1,fy-1,-1):
                path.append(board[ix][y])
            return path
        def vertical_up(ix,iy,fx,fy):
            #ix>fx,iy=fy
            for x in range(ix-1,fx-1,-1):
                path.append(board[x][iy])
            return path
        def vertical_down(ix,iy,fx,fy):
            #ix<fx,iy=fy
            for x in range(ix+1,fx+1):
                path.append(board[x][iy])
            return path
        def diagonal_upright(ix,iy,fx,fy):
            #ix>fx,iy<fy
            x = ix
            x-=1
            for y in range(iy+1,fy+1):
                path.append(board[x][y])
                x-=1
            return path
        def diagonal_upleft(ix,iy,fx,fy):
            #ix>fx,iy>fy
            x = ix
            x-=1
            for y in range(iy-1,fy-1,-1):
                path.append(board[x][y])
                x-=1
            return path
        def diagonal_downright(ix,iy,fx,fy):
            #ix<fx,iy<fy
            x=ix
            x+=1
            for y in range(iy+1,fy+1):
                path.append(board[x][y])
                x+=1
            return path
        def diagonal_downleft(ix,iy,fx,fy):
            #ix<fx,iy>fy
            x = ix
            x+=1
            for y in range(iy-1,fy-1,-1):
                path.append(board[x][y])
                x+=1
            return path
        
        if piece == 'kn':
            return True

        if piece == 'p':
            if initial_x < final_x:
                for i in range(initial_x+1,final_x+1):
                    path.append(board[i][initial_y])
            else:
                
                for i in range(initial_x-1,final_x-1,-1):
                    path.append(board[i][initial_y])

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
        print(path,'...path')
        return valid
            
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
        if((math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==1)or(math.fabs(final_x-initial_x)==0 and math.fabs(final_y-initial_y)==1)or(math.fabs(final_x-initial_x)==1 and math.fabs(final_y-initial_y)==0)):
            if IsEmpty(initial_x, initial_y, final_x, final_y):
                movement(initial_x,initial_y,final_x,final_y)

    #if pawn first move
    if board[initial_x][initial_y][0] == 'w' and board[initial_x][initial_y][1] == 'p' and initial_x==6:
        white_pawn_first_move(initial_x,initial_y,final_x,final_y)
    
    elif board[initial_x][initial_y][0] == 'b' and board[initial_x][initial_y][1] == 'p'and initial_x==1:
        black_pawn_first_move(initial_x,initial_y,final_x,final_y)\
    
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
        if board[black_kingx+1][black_kingy+1][:2] == 'wp':
            print('check1..',board[black_kingx+1][black_kingy+1])
            return 'black'
        #diagonal down left (black)
        elif board[black_kingx+1][black_kingy-1][:2] == 'wp':
            print('check2..',board[black_kingx+1][black_kingy-1])
            return 'black'
        #diagonal up right (white)
        elif board[white_kingx-1][white_kingy+1][:2] == 'bp':
            print('check3..',board[white_kingx-1][white_kingy+1])
            return 'white'
        #diagonal up left (black)
        elif board[white_kingx-1][white_kingy-1][:2] == 'bp':
            print('check4..',board[white_kingx-1][white_kingy-1])
            return 'white'
    
    def knight_check():
        def side(x,y,enemy):
            if x+2 < 8 and y+1 < 8:
                if board[x+2][y+1][:3] == enemy:
                    print('knight_check1..',board[x+2][y+1])
                    return True
            if x+2 < 8 and y-1 >= 0:
                if board[x+2][y-1][:3] == enemy:
                    print('knight_check2..',board[x+2][y-1])
                    return True
            if x+1 < 8 and y+2 < 8:
                if board[x+1][y+2][:3] == enemy:
                    print('knight_check3..',board[x+1][y+2])
                    return True
            if  x+1 < 8 and y-2 >= 0:
                if board[x+1][y-2][:3] == enemy:
                    print('knight_check4..',board[x+1][y-2])
                    return True
            if x-2 >= 0 and y+1 < 8:
                if board[x-2][y+1][:3] == enemy:
                    print('knight_check5..',board[x-2][y+1])
                    return True
            if x-2 >= 0 and y-1 < 8:
                if board[x-2][y-1][:3] == enemy:
                    print('knight_check6..',board[x-2][y-1])
                    return True
            if x-1 >= 0 and y+2 < 8:
                if board[x-1][y+2][:3] == enemy:
                    print('knight_check7..',board[x-1][y+2])
                    return True
            if x-1 >= 0 and y-2 >= 0:
                if board[x-1][y-2][:3] == enemy:
                    print('knight_check8..',board[x-1][y-2])
                    return True
        
        if side(black_kingx,black_kingy,'wkn'):
            return 'white'
        elif side(white_kingx,white_kingy,'bkn'):
            return 'black'
    
    
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
                    print('bishop_check1..',board[i][j])
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
                    print('bishop_check2..',board[i][j])
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
                    print('bishop_check3..',board[i][j])
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
                    print('bishop_check4..',board[i][j])
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
                    print('rook_check..',board[i][j])
                    k = 1
                    return True
                else:
                    break
            i,j = x,y
            while j<8 or k==1:
                if board[i][j] == ' ' or board[i][j]=='bk' or board[i][j]=='wk':
                    j+=1
                elif board[i][j][:2] == enemy:
                    print('rook_check..',board[i][j])
                    k = 1
                    return True
                else:
                    break
            i,j = x,y
            while i>=0 or k==1:
                if board[i][j] == ' ' or board[i][j]=='bk' or board[i][j]=='wk':
                    i-=1
                elif board[i][j][:2] == enemy:
                    print('rook_check..',board[i][j])
                    k = 1
                    return True
                else:
                    break
            i,j = x,y
            while j>=0 or k==1:
                if board[i][j] == ' ' or board[i][j]=='bk' or board[i][j]=='wk':
                    j-=1
                elif board[i][j][:2] == enemy:
                    print('rook_check..',board[i][j])
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
                
    
    #print(bishop_check())
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
                    if (turns%2==0 and board[clicked_coords[0]][clicked_coords[1]][0] == 'w') or (turns%2==1 and board[clicked_coords[0]][clicked_coords[1]][0] == 'b'):
                        initial_coordinates = clicked_coords
                        MovingPiece = board[clicked_coords[0]][clicked_coords[1]]
                        step = 1
                elif item !=' ' and step==1:
                    #if the piece they clicked on is of same colour as their initial click
                    MovingPiece = board[clicked_coords[0]][clicked_coords[1]]
                    if MovingPiece[0] == board[initial_coordinates[0]][initial_coordinates[1]][0]:
                        initial_coordinates = clicked_coords
                    else:
                        
                        fake_board = [i[:] for i in board]
                        fake_board[clicked_coords[0]][clicked_coords[1]] = MovingPiece
                        fake_board[initial_coordinates[0]][initial_coordinates[1]] = ' '
                        if Check(fake_board, MovingPiece) == 'black':
                            print('black is under check')
                        elif Check(fake_board,MovingPiece) == 'white':
                            print('white is under check')
                        
                        #this is if they try to capture a piece (click on their piece and then the enemy piece)

                        print(board[initial_coordinates[0]][initial_coordinates[1]],' captures ',board[clicked_coords[0]][clicked_coords[1]])

                        move(initial_coordinates,clicked_coords)
                        
            
                        step = 0
                        turns += 1

                elif item == ' ' and step == 1:
                    
                    fake_board = [i[:] for i in board]
                    fake_board[clicked_coords[0]][clicked_coords[1]] = MovingPiece
                    fake_board[initial_coordinates[0]][initial_coordinates[1]] = ' '

                    if Check(fake_board, MovingPiece) == 'black' and turns%2!=0:
                        print('black is under check')
                    elif Check(fake_board,MovingPiece) == 'white' and turns%2==0:
                        print('white is under check')
                    elif Check(fake_board,MovingPiece) == 'black' and turns%2==0:
                        print('black is under check')
                        print(initial_coordinates[0],initial_coordinates[1])
                        move(initial_coordinates,clicked_coords) 
                        step = 0
                        #turns += 1
                    elif Check(fake_board,MovingPiece) == 'white' and turns%2!=0:
                        print('white is under check')
                        print(initial_coordinates[0],initial_coordinates[1])
                        move(initial_coordinates,clicked_coords)
                        step = 0
                        #turns += 1
                    else:
                        print(initial_coordinates[0],initial_coordinates[1])
                        move(initial_coordinates,clicked_coords)
                        step = 0
                        #turns += 1
                
            except IndexError:
                pass
                
            #for i in board:
            #    print(i)





    pygame.display.update()