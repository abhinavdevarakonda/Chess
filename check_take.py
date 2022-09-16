def checkTake():
        IsEmpty(kingx,kingy,enemyx,enemyy)
        enemy_pos = path_pos[-1]
        x = enemy_pos[0]
        y = enemy_pos[1]
        if king == 'wk':
            team  = ['wp','wkn','wb','wr','wq']
        else:
            team = ['bp','bkn','bb','br','bq']
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j][:2],'..babu')
                if board[i][j][:2] == team[0]:
                    if capture_possibility(i,j,x,y):
                        return True
                elif board[i][j][:2] == team[1]:
                    if capture_possibility(i,j,x,y):
                        return True
                elif board[i][j][:2] == team[2]:
                    if capture_possibility(i,j,x,y):
                        return True
                elif board[i][j][:2] == team[3]:
                    if capture_possibility(i,j,x,y):
                        return True
                elif board[i][j][:2] == team[4]:
                    if capture_possibility(i,j,x,y):
                        return True
        return False
    