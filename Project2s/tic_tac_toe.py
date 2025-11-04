'''
Course: Introduction to Python Programming
'''
#%%
import random
from ComputerPlayer import ComputerPlayer
from tic_tac_toe_board_and_judge import *
from tic_tac_toe_board_and_judge import (DrawBoard, UpdateBoard, IsSpaceFree, Judge)
#%%
def HumanPlayer(Tag, Board, N=None):
    '''
    Parameters: 
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix
        N is a dumpy input
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
            0 <= row, col <= 2 
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        a while loop is needed, see HumanPlayer in rock-papper-scissors
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''
    #your code starts here
    while True:
        try:
            row = int(input("Please input the row index (0, 1, or 2): "))
            col = int(input("Please input the column index (0, 1, or 2): "))
            
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter values between 0 and 2.")
                continue

            from tic_tac_toe_board_and_judge import IsSpaceFree
            if not IsSpaceFree(Board, row, col):
                print("That spot is already occupied. Choose another one.")
                continue

            return (row, col)

        except ValueError:
            print("Invalid input. Please enter integer numbers only.")
    
#%%
def ShowOutcome(Outcome, NameX, NameO):
    '''
    Parameters:
        Outcome is from Judge
        NameX is a string, the name of PlayerX
        NameO is a string, the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
    Hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    '''
    #your code starts here

    if Outcome == 1:
        print(f"PlayerX ({NameX}, X) wins")
    elif Outcome == 2:
        print(f"PlayerO ({NameO}, O) wins")
    elif Outcome == 3:
        print("It is a tie")
    else:
        print("The game is still in progress")

#%% read but do not modify this function
def Which_Player_goes_first(ComputerPlayer, HumanPlayer):
    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''
    if random.randint(0, 1) == 0:
        print('Computer player goes first')        
        PlayerX = ComputerPlayer
        PlayerO = HumanPlayer
    else:
        print('Human player goes first')
        PlayerO = ComputerPlayer
        PlayerX = HumanPlayer
    return PlayerX, PlayerO
#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print('Wellcome to Tic Tac Toe Game')
    N=input('Set the steps for ComputerPlayer so that it could think N steps ahead: N=')
    try:
        N = int(N)
        if N < 0:
            print('N < 0, set it to 0')
            N=0
        if N > 1:
            print('N > 1, set it to 1')
            N=1
    except:
        print('invalid input, set N to 0')
        N = 0
    #an empty board
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    # determine the order
    PlayerX, PlayerO = Which_Player_goes_first(ComputerPlayer, HumanPlayer)
    # get the name of each function object
    # NameX and NameO are two strings, which could be 
    #   (1) 'ComputerPlayer' and 'HumanPlayer'    
    #   (2) 'HumanPlayer' and 'ComputerPlayer'
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    # while ???:
    # (1)  get a choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board, N)
    # (2)  update the Board
    # (3)  draw the Board
    # (4)  get the outcome from Judge
    # (5)  show the outcome
    # (6)  if the game is completed (win or tie), then break the loop
    # (7)  get a choice from PlayerO
    # (8)  update the Board
    # (9)  draw the Board
    # (10) get the outcome from Judge
    # (11) show the outcome
    # (12) if the game is completed (win or tie), then break the loop
    #---------------------------------------------------
    # do NOT modify the above code in TicTacToeGame
    # your code starts here
    while True:
        ChoiceX = PlayerX('X', Board, N)
        # update the Board
        Board[ChoiceX[0]][ChoiceX[1]] = 'X'
        #draw the Board
        DrawBoard(Board)
        #get the outcome
        outcome = Judge(Board)
        #show the outcome
        ShowOutcome(outcome, NameX, NameO)
#if game finished, break
        if outcome != 0:
            break
# get a choice from PlayerO
        ChoiceO = PlayerO('O', Board, N)
        # update the Board
        Board[ChoiceO[0]][ChoiceO[1]] = 'O'
        #draw the Board
        DrawBoard(Board)
        # get the outcome
        outcome = Judge(Board)
        # show the outcome
        ShowOutcome(outcome, NameX, NameO)
        #if game finished, break
        if outcome != 0:
            break
#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print('GameOver')
#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()

# %%
