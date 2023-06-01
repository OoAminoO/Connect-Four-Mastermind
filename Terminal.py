
import Utils

# -------------- Check the Winner Begins -------------- #
def checkWinner(positionNumber):
    # Horizontal check --
    x = positionNumber & (positionNumber >> 7)
    if x & (x >> 14):
        return True
    
    # Diagonal check \
    x = positionNumber & (positionNumber >> 6)
    if x & (x >> 12):
        return True
    
    # Diagonal check /
    x = positionNumber & (positionNumber >> 8)
    if x & (x >> 16):
        return True
    
    # Vertical check |
    x = positionNumber & (positionNumber >> 1)
    if x & (x >> 2):
        return True
    
    return False
# -------------- Check the Winner Ends -------------- #


def terminalAndScore(numericalAIPosition, numericalUserPosition) :
    # It returns a tuple of (isTerminal, score)
    
    AIWin   = checkWinner(numericalAIPosition)
    userWin = checkWinner(numericalUserPosition)
    if AIWin :
        return (1, 1)       # AI won the game so this state is terminal
    elif userWin :
        return (1, -1)      # AI or User won the game so this state is terminal
    elif numericalAIPosition | numericalUserPosition == 279258638311359 :
        return (1, 0)       # AI or User didn't win the game but there is no empty cell so this state is terminal
    return (0, 0)           # AI or User didn't win the game and there is empty cell so this state is not terminal


# 1010 -> 1 is most significant, 0 is least significant --- board[48] -> ms, board[0] -> ls


# At the end of the game, when the game has a winner,
#    this function determines which four pieces are connected,
#    so that they can be starred
def winningPieces(lastPieceIndex, board, turn):
    # Horizontal check --
    possiblePieces = [lastPieceIndex + 7 * i for i in range(-3, 4) if lastPieceIndex + 7 * i <= 48 and lastPieceIndex + 7 * i >= 0]
    for i in range(len(possiblePieces) - 3):
        if board[possiblePieces[i]] == board[possiblePieces[i + 1]] == board[possiblePieces[i + 2]] == board[possiblePieces[i + 3]] == turn:
            return possiblePieces[i], possiblePieces[i + 1], possiblePieces[i + 2], possiblePieces[i + 3]
    
    # Diagonal check /
    column = lastPieceIndex // 7
    possiblePieces = [lastPieceIndex + 8 * i for i in range(-3, 4) if lastPieceIndex + 8 * i <= 48 and lastPieceIndex + 8 * i >= 0 and (lastPieceIndex + 8 * i) // 7 == column + i]
    for i in range(len(possiblePieces) - 3):
        if board[possiblePieces[i]] == board[possiblePieces[i + 1]] == board[possiblePieces[i + 2]] == board[possiblePieces[i + 3]] == turn:
            return possiblePieces[i], possiblePieces[i + 1], possiblePieces[i + 2], possiblePieces[i + 3]

    # Diagonal check \
    column = lastPieceIndex // 7
    possiblePieces = [lastPieceIndex + 6 * i for i in range(-3, 4) if lastPieceIndex + 6 * i <= 48 and lastPieceIndex + 6 * i >= 0 and (lastPieceIndex + 6 * i) // 7 == column + i]
    for i in range(len(possiblePieces) - 3):
        if board[possiblePieces[i]] == board[possiblePieces[i + 1]] == board[possiblePieces[i + 2]] == board[possiblePieces[i + 3]] == turn:
            return possiblePieces[i], possiblePieces[i + 1], possiblePieces[i + 2], possiblePieces[i + 3]

    # Vertical check |
    possiblePieces = [lastPieceIndex + i for i in range(-3, 1) if (lastPieceIndex + i) // 7 == lastPieceIndex // 7]
    for i in range(len(possiblePieces) - 3):
        if board[possiblePieces[i]] == board[possiblePieces[i + 1]] == board[possiblePieces[i + 2]] == board[possiblePieces[i + 3]] == turn:
            return possiblePieces[i], possiblePieces[i + 1], possiblePieces[i + 2], possiblePieces[i + 3]



