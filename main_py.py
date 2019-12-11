#Othello
def check_sel(board,x,y):
    try :
        if board[x][y]=='●'
            if board[x-1][y-1]=='○':return True
            if board[x-1][y+1]=='○':return True
            if board[x][y-1]=='○':return True
            if board[x][y+1]=='○':return True
            if board[x+1][y-1]=='○':return True
            if board[x+1][y]=='○':return True
            if board[x+1][y+1]=='○':return True
        if board[x][y]=='○'
            if board[x-1][y-1]=='●':return True
            if board[x-1][y]=='●':return True
            if board[x-1][y+1]=='●':return True
            if board[x][y-1]=='●':return True
            if board[x][y+1]=='●':return True
            if board[x+1][y-1]=='●':return True
            if board[x+1][y]=='●':return True
            if board[x+1][y+1]=='●':return True
def show_board(board):
    k_1=['①','②','③','④','⑤','⑥','⑦','⑧']
    i=0
    print()
    print('*','|','①',' ②',' ③',' ④',' ⑤',' ⑥',' ⑦',' ⑧')
    print('-','+','-','-','-','-','-','-','-','-','-','-','-','-')
    while i<8:
	    print(k_1[i],'|',board[i][0],board[i][1],board[i][2]\
				,board[i][3],board[i][4],board[i][5],board[i][6]\
				,board[i][7])
	    i+=1
    print()
def create_board():#creating board array
    board=[[],[],[],[],[],[],[],[]]
    for i in range(0,8):
        for j in range(0,8):
             board[i].append('ㆍ')
    board[3][4]='●'
    board[4][3]='●'
    board[3][3]='○'
    board[4][4]='○'
    return board
def cordinate_board(message,i,j):#receiving cordinate
    while True:
        try :
            number = input(message+' ')
            while not int(number) in range(i,j+1): 
                number = input('\nType the number in range.\n\n'+ message)
            break
        except ValueError:
            print('\nType in the Integer value.\n\n')
        except KeyboardInterrupt:
            choice=input('\nSurrender(y/n):')
            if choice=='y':
                print('\nSurrender\n')
                return -1
            else:
                continue
    return int(number)-1
def surrender(num):
    if num == -1:
	    print("surrender")
	    return True
def othello():#surrender, score check, turn change, setting piece
    board = create_board()
    show_board(board)
    while True :
        while True:
            cord_x = cordinate_board("row number(1~8):",1,8)
            if surrender(cord_x):
                break
            cord_y = cordinate_board("column number(1~8):",1,8)
            if surrender(cord_y):
                break
            if board[cord_x][cord_y]=='ㆍ':
    	        board[cord_x][cord_y]= '●'
    	        show_board(board)
    	        break
            else:
                continue
        while True:
            cord_x = cordinate_board("row number(1~8):",1,8)
            if surrender(cord_x):
                break
            cord_y = cordinate_board("column number(1~8):",1,8)
            if surrender(cord_y):
                break
            if board[cord_x][cord_y]:
                board[cord_x][cord_y]= '○'
                show_board(board)
                break
            else:
                continue
othello()
