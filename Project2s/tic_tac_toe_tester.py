from copy import deepcopy
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--student', type=str, default='tic_tac_toe')
arg=parser.parse_args()
print(arg)
#%%
exec ("import "+arg.student+" as student")
exec ("from "+arg.student+" import TicTacToeGame, DrawBoard")
exec ("from "+arg.student+" import HumanPlayer as human_player")
#%% manually test HumanPlayer (15 points)
Board7 = [['O', 'X', 'O'],
          [' ', 'X', 'X'],
          [' ', 'O', 'X']]
DrawBoard(Board7)
human_player("O", Board7)
#play it and assign the score, max=15. 
#-10 if human_player cannot handled/do not check invalid input
score8=15
#%% manually test TicTacToeGame (10 points), ShowOutcome (5 points), and DrawBoard (5 points)
score0=10
try:
    student.HumanPlayer= student.ComputerPlayer
    TicTacToeGame()
except:
    score0=0
#-5 if some messages are missing (e.g., who wins the game)
#look at the output and assign the scores
score_showoutcome=5
score_drawboard=5
#%%
print("TicTacToeGame score=",score0)    
print('HumanPlayer score=', score8)
print('ShowOutcome score=', score_showoutcome)
print('DrawBoard score=', score_drawboard)
#%%
exec ("from "+arg.student+" import IsSpaceFree as is_space_free")
exec ("from "+arg.student+" import GetNumberOfChessPieces as get_number_of_chess_pieces")
exec ("from "+arg.student+" import IsBoardFull as is_board_full")
exec ("from "+arg.student+" import IsBoardEmpty as is_board_empty")
exec ("from "+arg.student+" import UpdateBoard as update_board")
exec ("from "+arg.student+" import ComputerPlayer as computer_player")
exec ("from "+arg.student+" import Judge as judge")
exec ("from "+arg.student+" import Judge as judge")
#%%
Board0 = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]
Board1 = [[' ', ' ', ' '],
          [' ', 'X', ' '],
          [' ', ' ', ' ']]
Board2 = [['O', ' ', ' '],
          [' ', 'X', ' '],
          [' ', ' ', ' ']]
Board3 = [['O', ' ', ' '],
          [' ', 'X', ' '],
          [' ', ' ', 'X']]
Board4 = [['O', ' ', 'O'],
          [' ', 'X', ' '],
          [' ', ' ', 'X']]
Board5 = [['O', 'X', 'O'],
          [' ', 'X', ' '],
          [' ', ' ', 'X']]
Board6 = [['O', 'X', 'O'],
          [' ', 'X', ' '],
          [' ', 'O', 'X']]
Board7 = [['O', 'X', 'O'],
          [' ', 'X', 'X'],
          [' ', 'O', 'X']]
Board8 = [['O', 'X', 'O'],
          ['O', 'X', 'X'],
          [' ', 'O', 'X']]
Board9 = [['O', 'X', 'O'],
          ['O', 'X', 'X'],
          ['X', 'O', 'X']]
#%% test IsSpaceFree
score1=5
try:
    for i in range(0, 3):
        for j in range(0, 3):
            if is_space_free(deepcopy(Board0), i, j) != True:
                score1=0
                break
        if score1 == 0:
            break
    for i in range(0, 3):
        for j in range(0, 3):
            if is_space_free(deepcopy(Board9), i, j) != False:
                score1=0
                break
        if score1==0:
            break
    for i in range(-100, -1):
        for j in range(-100, -1):
            if is_space_free(deepcopy(Board0), i, j) != False:
                score1=0      
                break
        if score1==0:
            break
except:
    score1=0
print("IsSpaceFree: score=", score1)
#%% test GetNumberOfChessPieces (5 points)
score2=5
for k in range(0, 10):
    if get_number_of_chess_pieces(deepcopy((eval("Board"+str(k))))) != k:
        score2=0
        break
print("GetNumberOfChessPieces: score=", score2)
#%% test IsBoardFull (2 points)
score3=2
if is_board_full(Board9) != True:
    score3=0
for k in range(0, 9):
    if is_board_full(deepcopy(eval("Board"+str(k)))) != False:
        score3=0
        break
print("IsBoardFull: score=", score3)  
#%% test IsBoardEmpy (3 points)
score4=3
if is_board_empty(Board0) != True:
    score4=0
for k in range(1, 10):
    if is_board_empty(deepcopy(eval("Board"+str(k)))) != False:
        score4=0
        break
print("IsBoardEmpy: score=", score4)  
#%% test UpdateBoard (5 points)
score5=5
try:
    for i in range(0, 3):
        for j in range(0, 3):
            temp=deepcopy(Board0)
            update_board(temp, "X", (i,j))
            if temp[i][j] != "X":
                score5=0
                break
            temp=deepcopy(Board0)
            update_board(temp, "O", (i,j))
            if temp[i][j] != "O":
                score5=0
                break
        if score5==0:
            break
except:
    score5=0
print("UpdateBoard: score=", score5)
#%% test ComputerPlayer (5 points for random play)
score6a=5
for k in range(1, 9):
    board_k=deepcopy(eval("Board"+str(k)))
    i, j=computer_player("X", board_k, N=0)
    if (i not in [0, 1, 2]) or (j not in [0, 1, 2]):
        score6a=0
        print("ComputerPlayer(N=0): error 0")
        break
    if board_k[i][j] != " ":
        score6a=0
        print("ComputerPlayer(N=0): error 1")
        break
    if board_k != eval("Board"+str(k)):
        score6a=0
        print("ComputerPlayer(N=0): error 2")
        break
    i, j=computer_player("O", board_k, N=0)
    if (i not in [0, 1, 2]) or (j not in [0, 1, 2]):
        score6a=0
        print("ComputerPlayer(N=0): error 3")
        break
    if board_k[i][j] != " ":
        score6a=0
        print("ComputerPlayer(N=0): error 4")
        break
    if board_k != eval("Board"+str(k)):
        score6a=0
        print("ComputerPlayer(N=0): error 5")
        break
#%% test ComputerPlayer (25 points for thinking one-step ahead)    
#---------------------------
score6b=25
#---------------------------
Board = [['X', ' ', ' '],
         [' ', 'O', ' '],
         ['X', ' ', ' ']]
choice=computer_player("O", Board, N=1)
if list(choice) != [1,0]:
    score6b=0
    print("ComputerPlayer(N=1): error 0")
#%%
Board = [['O', ' ', 'X'],
         [' ', ' ', ' '],
         ['X', ' ', ' ']]
choice=computer_player("O", Board, N=1)
if list(choice) != [1,1]:
    score6b=0
    print("ComputerPlayer(N=1): error 1")
#%%
Board = [['X', ' ', ' '],
         [' ', 'X', ' '],
         ['O', ' ', ' ']]
choice=computer_player("O", Board, N=1)
if list(choice) != [2,2]:
    score6b=0
    print("ComputerPlayer(N=1): error 2")
#%%
Board = [['X', ' ', 'X'],
         [' ', 'X', ' '],
         ['O', ' ', 'O']]
choice=computer_player("O", Board, N=1)
if list(choice) != [2,1]:
    score6b=0
    print("ComputerPlayer(N=1): error 3")
#%%
Board = [['O', ' ', 'X'],
         [' ', 'X', ' '],
         [' ', ' ', 'O']]
choice=computer_player("X", Board, N=1)
if list(choice) != [2,0]:
    score6b=0
    print("ComputerPlayer(N=1): error 4")
#%%
Board = [['O', 'X', ' '],
         [' ', 'X', ' '],
         [' ', ' ', 'O']]
choice=computer_player("X", Board, N=1)
if list(choice) != [2,1]:
    score6b=0
    print("ComputerPlayer(N=1): error 5")
#%%
Board = [['X', 'O', ' '],
         ['X', ' ', ' '],
         [' ', ' ', 'O']]
choice=computer_player("X", Board, N=1)
if list(choice) != [2,0]:
    score6b=0
    print("ComputerPlayer(N=1): error 6")
#%%
Board = [['X', ' ', 'X'],
         ['O', ' ', 'O'],
         [' ', ' ', ' ']]
choice=computer_player("X", Board, N=1)
if list(choice) != [0,1]:
    score6b=0
    print("ComputerPlayer(N=1): error 7")
#%%    
score6=score6a+score6b
print("ComputerPlayer: score=", score6)
#%% --------------------- test Judge (15 points) ------------------------------
#Outcome is 0 if the game is still in progress
#Outcome is 1 if player X wins
#Outcome is 2 if player O wins
#Outcome is 3 if it is a tie (no winner)
score7=15
#%%
for k in range(0, 9):
    if judge(eval("Board"+str(k))) != 0:
        score7=0
        print('Judge: error 0a')
        break
#%%
if judge(Board9) != 3:
    score7=0
    print('Judge: error 0b')
#%%    
Board = [['X', 'X', 'X'],
         ['O', ' ', 'O'],
         [' ', ' ', ' ']]
if judge(Board) != 1:
    score7=0
    print('Judge: error 1')
#%%
Board = [[' ', ' ', ' '],
         ['X', 'X', 'X'],
         ['O', ' ', 'O']]
if judge(Board) != 1:
    score7=0
    print('Judge: error 2')
#%%
Board = [[' ', ' ', ' '],
         ['O', ' ', 'O'],
         ['X', 'X', 'X']]
if judge(Board) != 1:
    score7=0
    print('Judge: error 3')
#%%
Board = [['X', 'O', ' '],
         ['X', ' ', 'O'],
         ['X', ' ', ' ']]
if judge(Board) != 1:
    score7=0
    print('Judge: error 4')
#%%
Board = [['O', 'X', ' '],
         [' ', 'X', 'O'],
         [' ', 'X', ' ']]
if judge(Board) != 1:
    score7=0
#%%
Board = [['O', ' ', 'X'],
         [' ', ' ', 'X'],
         [' ', 'O', 'X']]
if judge(Board) != 1:
    score7=0
    print('Judge: error 5')
#%%
Board = [[' ', ' ', 'X'],
         ['O', 'X', 'O'],
         ['X', ' ', ' ']]
if judge(Board) != 1:
    score7=0
    print('Judge: error 6')
#%%
Board = [['X', ' ', ' '],
         ['O', 'X', 'O'],
         [' ', ' ', 'X']]
if judge(Board) != 1:
    score7=0
    print('Judge: error 7')
#%%
Board = [['X', 'X', 'O'],
         ['X', 'O', 'O'],
         ['X', 'O', 'X']]
if judge(Board) != 1:
    score7=0
    print('Judge: error 8')
#%%
Board = [['X', ' ', 'X'],
         ['X', ' ', ' '],
         ['O', 'O', 'O']]
if judge(Board) != 2:
    score7=0
    print('Judge: error 9')
#%%
Board = [['X', ' ', 'X'],
         ['O', 'O', 'O'],
         ['X', ' ', ' ']]
if judge(Board) != 2:
    score7=0
    print('Judge: error 10')
#%%    
Board = [['O', 'O', 'O'],
         ['X', ' ', ' '],
         ['X', ' ', 'X']]
if judge(Board) != 2:
    score7=0
    print('Judge: error 11')
#%%
Board = [['O', 'X', 'X'],
         ['O', ' ', ' '],
         ['O', ' ', 'X']]
if judge(Board) != 2:
    score7=0
    print('Judge: error 12')
#%%
Board = [['X', 'O', 'X'],
         [' ', 'O', ' '],
         [' ', 'O', 'X']]
if judge(Board) != 2:
    score7=0
    print('Judge: error 13')
#%%
Board = [['X', 'X', 'O'],
         [' ', ' ', 'O'],
         ['X', ' ', 'O']]
if judge(Board) != 2:
    score7=0
    print('Judge: error 14')
#%%
Board = [['O', 'X', 'X'],
         [' ', 'O', ' '],
         ['X', ' ', 'O']]
if judge(Board) != 2:
    score7=0
    print('Judge: error 15')
#%%
Board = [['X', 'X', 'O'],
         [' ', 'O', ' '],
         ['O', ' ', 'X']]
if judge(Board) != 2:
    score7=0
    print('Judge: error 16')
#%%
Board = [['X', 'X', 'O'],
         ['X', 'O', 'O'],
         ['O', 'X', 'X']]
if judge(Board) != 2:
    score7=0
    print('Judge: error 17')
#%%
print("Judge: score=", score7)    
#%%
score=score0+score1+score2+score3+score4+score5+score6+score7+score8
score+=score_showoutcome+score_drawboard
print("total score (100)=", score)    
    


