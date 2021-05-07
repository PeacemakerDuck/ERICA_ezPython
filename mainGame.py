#Othello
import tiktakto_func
def tiktakto():#surrender, score check, turn change, setting piece
    board = create_board()
    row = load_quiz()
    load(2)
    print("\n___---TIK-TAK-TO---___\n")
    time.sleep(1)
    print("\n-> Loading\n")
    load(3)
    show_board(board)
    while True :
        if check_scr(board)!= None:
            break
        while True:
            print("플레이어 ●  차례")
            cord_x = cordinate_board("세로 번호(1~8):",1,8)
            if surrender('○ ',"● ",cord_x):
                return
            cord_y = cordinate_board("가로 번호(1~8):",1,8)
            if surrender('○ ',"● ",cord_y):
                return
            if board[cord_x][cord_y]=='ㆍ':
                if quiz(row)==True:
    	            board[cord_x][cord_y]= '● '
    	            show_board(board)
    	            break
                else:
                    print("\n## 답이 틀렸습니다! 상대편의 돌이 놓아집니다. ##")
                    time.sleep(1)
                    board[cord_x][cord_y]= '○ '
                    show_board(board)
                    break
            else:
                print("\n##이미 돌이 놓여있는 위치입니다.##\n")
                continue
        if check_scr(board)!= None:
            break
        while True:
            if check_scr(board)!= None:
                break
            print("플레이어 ○  차례")
            cord_x = cordinate_board("세로 번호(1~8):",1,8)
            if surrender("● ",'○ ',cord_x):
                return
            cord_y = cordinate_board("가로 번호(1~8):",1,8)
            if surrender("● ",'○ ',cord_y):
                return
            if board[cord_x][cord_y]=='ㆍ':
                if quiz(row)==True:
                    board[cord_x][cord_y]= '○ '
                    show_board(board)
                    break
                else:
                    print("\n## 답이 틀렸습니다! 상대편의 돌이 놓아집니다. ##\n")
                    time.sleep(1)
                    board[cord_x][cord_y]= '● '
                    show_board(board)
                    break
            else:
                print("\n##이미 돌이 놓여있는 위치입니다.##\n")
                continue
            if check_scr(board)!= None:
                break
        if check_scr(board)!= None:
            break
def othello():#surrender, score check, turn change, setting piece
    board = create_board()
    row = load_quiz()
    load(2)
    print("\n___---TIK-TAK-TO---___\n")
    time.sleep(1)
    print("\n-> Loading\n")
    load(3)
    show_board(board)
    while True :
        if check_scr(board)!= None:
            break
        while True:
            print("플레이어 ●  차례")
            cord_x = cordinate_board("세로 번호(1~8):",1,8)
            if surrender('○ ',"● ",cord_x):
                return
            cord_y = cordinate_board("가로 번호(1~8):",1,8)
            if surrender('○ ',"● ",cord_y):
                return
            if board[cord_x][cord_y]=='ㆍ':
                if quiz(row)==True:
    	            board[cord_x][cord_y]= '● '
    	            show_board(board)
    	            break
                else:
                    print("\n## 답이 틀렸습니다! 상대편의 돌이 놓아집니다. ##")
                    time.sleep(1)
                    board[cord_x][cord_y]= '○ '
                    show_board(board)
                    break
            else:
                print("\n##이미 돌이 놓여있는 위치입니다.##\n")
                continue
        if check_scr(board)!= None:
            break
        while True:
            if check_scr(board)!= None:
                break
            print("플레이어 ○  차례")
            cord_x = cordinate_board("세로 번호(1~8):",1,8)
            if surrender("● ",'○ ',cord_x):
                return
            cord_y = cordinate_board("가로 번호(1~8):",1,8)
            if surrender("● ",'○ ',cord_y):
                return
            if board[cord_x][cord_y]=='ㆍ':
                if quiz(row)==True:
                    board[cord_x][cord_y]= '○ '
                    show_board(board)
                    break
                else:
                    print("\n## 답이 틀렸습니다! 상대편의 돌이 놓아집니다. ##\n")
                    time.sleep(1)
                    board[cord_x][cord_y]= '● '
                    show_board(board)
                    break
            else:
                print("\n##이미 돌이 놓여있는 위치입니다.##\n")
                continue
            if check_scr(board)!= None:
                break
        if check_scr(board)!= None:
            break
tiktakto()
