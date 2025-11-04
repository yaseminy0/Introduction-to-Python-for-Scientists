
import random
import copy
from tic_tac_toe_board_and_judge import (IsBoardEmpty, IsSpaceFree, Judge)
#%%
def ComputerPlayer(Tag, Board, N):
    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer is PlayerX who goes first
        Board is the game board, a 3x3 matrix (nested list)
        N: think N steps ahead, 0 or 1
    Return: (row, col), a choice of the ComputerPlayer
            0 <= row <=2, 0 <= col <= 2 
    Description:
        if N == 0:
            a random strategy in a while loop:
                (1) randomly choose a spot on the Board
                (2) if the spot is empty then return (row, col) of the spot
                (3) if the spot is not empty then go to (1)
        if N == 1:
            think 1 step ahead            
    Attention:
        Board is NOT modified in this function
    '''
    #your code starts here
    if N == 0:
        # random strategy in a while loop
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if IsSpaceFree(Board, r, c):
                return (r, c)

    if N == 1:
        # (1) win if possible
        for r in range(3):
            for c in range(3):
                if IsSpaceFree(Board, r, c):
                    trial = copy.deepcopy(Board)
                    trial[r][c] = Tag
                    outcome = Judge(trial)
                    if (Tag == 'X' and outcome == 1) or (Tag == 'O' and outcome == 2):
                        return (r, c)

        # (2) otherwise block opponent's immediate win
        opp = 'O' if Tag == 'X' else 'X'
        for r in range(3):
            for c in range(3):
                if IsSpaceFree(Board, r, c):
                    trial = copy.deepcopy(Board)
                    trial[r][c] = opp
                    outcome = Judge(trial)
                    if (opp == 'X' and outcome == 1) or (opp == 'O' and outcome == 2):
                        return (r, c)

        # (3) else random strategy in a while loop
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if IsSpaceFree(Board, r, c):
                return (r, c)          
                
        
    
   
        
        
        
# %%
