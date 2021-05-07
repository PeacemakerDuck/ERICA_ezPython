import time
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
    num = random.randrange(1,33)
    if 22>num>11:
        b=random.randrange(11,45)
        c=random.randrange(50,100)
        answer = repr(b*c)
        if input("산수 :"+repr(b)+"x"+repr(c)+"= ?")==answer:
            return True
        else: return False
    elif num>21:
        b=random.randrange(555,2333)
        c=random.randrange(111,444)
        answer = repr(b-c)
        if input("산수 :"+repr(b)+"-"+repr(c)+"= ?")==answer:
            return True
        else: return False
    else:
        quiz = row[repr(num)]
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
            elif board[i+1][j-1]==board[i][j]==board[i-1][j+1]=='● ':
                print('플레이어 ●  승리!')
                return '●'
            elif board[i-1][j-1]==board[i][j]==board[i+1][j+1]=='○ ':
                print('플레이어 ○  승리!')
                return '○'
            elif board[i+1][j-1]==board[i][j]==board[i-1][j+1]=='○ ':
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
    print("-> ctrl+c = 항복")
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
                number = input('\n범위안의 숫자를 입력하세요.\n\n'+ message)
            break
        except ValueError:
            print('\n정수값을 입력하세요.\n\n')
        except KeyboardInterrupt:
            choice=input('\n항복하시겠습니까?(y/n):')
            if choice=='y':
                return -1
            else:
                continue
    return int(number)-1
def load(n):
    if n>0:
        print("-> ....")
        time.sleep(1)
        load(n-1)
    else:
        return
def surrender(win,lose,num):
    if num == -1:
	    print("\n플레이어"+lose+"이 항복했습니다.\n\n플레이어"+win+"승리!")
	    return True
