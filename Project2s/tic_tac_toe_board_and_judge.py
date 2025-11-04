#%%
def DrawBoard(Board):
    '''
    Parameters: Board is the game board, a 3x3 matrix (nested list)
    Return: None
    Description: this funcion will draw the game board using print
    example:
        O|X|X
        -+-+-
        X|X|O
        -+-+-
        O|O|X
    '''
    #your code starts here
    
    for i in range(3):
        print(f"{Board[i][0]}|{Board[i][1]}|{Board[i][2]}")
        if i < 2:
            print("-+-+-")
    return None
            
#%% 
def IsSpaceFree(Board, i ,j):
    '''
    Parameters: Board is the game board, a 3x3 matrix (nested list)
                i is the row index, j is the col index
    Return: True or False    
    Description:
        valid range: 0 <= i <=2, 0<= j <= 2
        (1) return False if i or j is invalid (e.g. i = -1 or 100)
        (2) return True  if Board[i][j] is empty (' ') - one single blank space
        (3) return False if Board[i][j] is not empty
    Do NOT use print in this function
    '''
    #your code starts here
    if not (0 <= i <= 2 and 0 <= j <= 2):
        return False
    return Board[i][j] == ' '
        
#%%
def GetNumberOfChessPieces(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix (nested list)
    Return: the number of chess piceces on Board
            i.e. the total number of 'X' and 'O'
    Hint: define a counter and use a nested for loop, like this
          for i in 0 to 3
              for j in 0 to 3
                  add one to the counter if Board[i][j] is not empty
    '''
    #your code starts here
    counter = 0
    for i in range(3):
        for j in range(3):
            if Board[i][j] != ' ':
                counter+=1
    return counter
#%%
def IsBoardFull(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix (nested list)
    Return: True or False
    Description: 
        return True if the Board is fully occupied
        return False otherwise 
    Hint: use GetNumberOfChessPieces
    '''
    #your code starts here
    if GetNumberOfChessPieces(Board) == 9:
        return True
    else:
        return False
    
#%%
def IsBoardEmpty(Board):
    '''
    Parameter: Board is the game board, a 3x3 matrix (nested list)
    Return: True or False
    Description: 
        return True if the Board is empty
        return False otherwise 
    Hint: use GetNumberOfChessPieces
    '''
    #your code starts here
    if GetNumberOfChessPieces(Board) == 0:
        return True
    else:
        return False
#%%
def UpdateBoard(Board, Tag, Choice):
    '''
    Parameters: 
        Board is the game board, a 3x3 matrix (nested list)
        Tag is 'O' or 'X'
        Choice is a tuple (row, col) from HumanPlayer or ComputerPlayer
    Return: None
    Description: 
         Update the Board after a player makes a choice
         Set an element of the Board to Tag at the location (row, col)
    '''
    #your code starts here
    row, col = Choice
    if 0 <= row <= 2 and 0 <= col <= 2 and Board[row][col] == ' ' and Tag in ('X', 'O'):
        Board[row][col] = Tag
        return True
    return False
#%%
def Judge(Board):
    '''
    Parameter:
         Board is the current game board, a 3x3 matrix (nested list)
    Return: Outcome, an integer
        Outcome is 0 if the game is still in progress
        Outcome is 1 if player X wins
        Outcome is 2 if player O wins
        Outcome is 3 if it is a tie (no winner)
    Description:
        this funtion determines the Outcome of the game
    Hint:
        (1) check if anyone wins, i.e., if three 'X' or 'O' in
            top row, middle row, bottom row
            lef col, middle col, right col
            two diagonals
        (2) if no one wins, then check if it is a tie
            note: if the board is fully occupied, then it is a tie
        (3) otherwise, the game is still in progress
    '''
    #your code starts here
        
    Outcome = 0
    
    lines = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]

    for line in lines:
        a, b, c = [Board[r][c] for r, c in line]
        if a != ' ' and a == b == c:
            if a == 'X':
                Outcome = 1
            elif a == 'O':
                Outcome = 2
            return Outcome  

    if IsBoardFull(Board):
        Outcome = 3
    else:
        Outcome = 0

    return Outcome

# %%
