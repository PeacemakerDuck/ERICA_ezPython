#Othello
import random
def load_quiz():
    file = open("quiz.txt","r")
    row = {}
    for line in file:
        no, quiiz, answer = line.strip('\n').split(',')
        row[no] = [quiiz,answer]
    file.close()
    return row
def quiz(row):
    quiz = row[repr(random.randrange(1,4))]
    answer = quiz[1]
    if input(quiz[0])==answer:
        return True
    else:
        return False
def check_scr(board):
    for i in range(0,8):
        for j in range(1,7):
            if board[i][j]==board[i][j-1]==board[i][j+1]=='● ':
                print('플레이어 ●  승리!')
                return '●'
            elif board[i][j]==board[i][j-1]==board[i][j+1]=='○ ':
                print('플레이어 ○  승리!')
                return '○'
    for i in range(1,7):
        for j in range(0,8):
            if board[i-1][j]==board[i][j]==board[i+1][j]=='● ':
                print('플레이어 ●  승리!')
                return '●'
            elif board[i-1][j]==board[i][j]==board[i+1][j]=='○ ':
                print('플레이어 ○  승리!')
                return '○'
    for i in range(1,7):
        for j in range(1,7):
            if board[i-1][j-1]==board[i][j]==board[i+1][j+1]=='● ':
                print('플레이어 ●  승리!')
                return '●'
            elif board[i+1][j-1]==board[i][j]==board[i-1][j+1]=='●':
                print('플레이어 ●  승리!')
                return '●'
            elif board[i-1][j-1]==board[i][j]==board[i+1][j+1]=='○':
                print('플레이어 ○  승리!')
                return '○'
            elif board[i+1][j-1]==board[i][j]==board[i-1][j+1]=='○':
                print('플레이어 ○  승리!')
                return '○'
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
    row = load_quiz()
    while True :
        if check_scr(board)!= None:
            break
        while True:
            print("플레이어 ●  차례")
            cord_x = cordinate_board("세로 번호(1~8):",1,8)
            if surrender(cord_x):
                break
            cord_y = cordinate_board("가로 번호(1~8):",1,8)
            if surrender(cord_y):
                break
            if board[cord_x][cord_y]=='ㆍ':
                if quiz(row)==True:
    	            board[cord_x][cord_y]= '● '
    	            show_board(board)
    	            break
                else:
                    print("Wrong!")
                    board[cord_x][cord_y]= '○ '
                    show_board(board)
                    break
            else:
                continue
        if check_scr(board)!= None:
            break
        while True:
            if check_scr(board)!= None:
                break
            print("플레이어 ○  차례")
            cord_x = cordinate_board("세로 번호(1~8):",1,8)
            if surrender(cord_x):
                break
            cord_y = cordinate_board("가로 번호(1~8):",1,8)
            if surrender(cord_y):
                break
            if board[cord_x][cord_y]:
                if quiz(row)==True:
                    board[cord_x][cord_y]= '○ '
                    show_board(board)
                    break
                else:
                    print("Wrong!")
                    board[cord_x][cord_y]= '● '
                    show_board(board)
                    break
            else:
                continue
            if check_scr(board)!= None:
                break
        if check_scr(board)!= None:
            break
othello()
