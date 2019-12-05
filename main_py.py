#Othel
def show_board(board):
    k_1=['①','②','③','④','⑤','⑥','⑦','⑧']
    i=0
    print()
    print('*','|','①','②','③','④','⑤','⑥','⑦','⑧')
    print('*','+','-','-','-','-','-','-','-','-')
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
def orthello():
	pass
board = create_board()
show_board(board)
