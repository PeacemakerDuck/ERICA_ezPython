#Othello
import ttt_f #tiktakto function
import time
def tiktakto():#surrender, score check, turn change, setting piece
    board = ttt_f.create_board()
    row = ttt_f.load_quiz()
    ttt_f.load(2)
    print("\n___---TIK-TAK-TO---___\n")
    time.sleep(1)
    print("\n-> Loading\n")
    ttt_f.load(3)
    ttt_f.show_board(board)
    while True :
        if ttt_f.check_scr(board)!= None:
            break
        while True:
            print("플레이어 ●  차례")
            cord_x = ttt_f.cordinate_board("세로 번호(1~8):",1,8)
            if ttt_f.surrender('○ ',"● ",cord_x):
                return
            cord_y = ttt_f.cordinate_board("가로 번호(1~8):",1,8)
            if ttt_f.surrender('○ ',"● ",cord_y):
                return
            if board[cord_x][cord_y]=='ㆍ':
                if ttt_f.quiz(row)==True:
    	            board[cord_x][cord_y]= '● '
    	            ttt_f.show_board(board)
    	            break
                else:
                    print("\n## 답이 틀렸습니다! 상대편의 돌이 놓아집니다. ##")
                    time.sleep(1)
                    board[cord_x][cord_y]= '○ '
                    ttt_f.show_board(board)
                    break
            else:
                print("\n##이미 돌이 놓여있는 위치입니다.##\n")
                continue
        if ttt_f.check_scr(board)!= None:
            break
        while True:
            if ttt_f.check_scr(board)!= None:
                break
            print("플레이어 ○  차례")
            cord_x = ttt_f.cordinate_board("세로 번호(1~8):",1,8)
            if ttt_f.surrender("● ",'○ ',cord_x):
                return
            cord_y = ttt_f.cordinate_board("가로 번호(1~8):",1,8)
            if ttt_f.surrender("● ",'○ ',cord_y):
                return
            if board[cord_x][cord_y]=='ㆍ':
                if ttt_f.quiz(row)==True:
                    board[cord_x][cord_y]= '○ '
                    ttt_f.show_board(board)
                    break
                else:
                    print("\n## 답이 틀렸습니다! 상대편의 돌이 놓아집니다. ##\n")
                    time.sleep(1)
                    board[cord_x][cord_y]= '● '
                    ttt_f.show_board(board)
                    break
            else:
                print("\n##이미 돌이 놓여있는 위치입니다.##\n")
                continue
            if ttt_f.check_scr(board)!= None:
                break
        if ttt_f.check_scr(board)!= None:
            break
tiktakto()