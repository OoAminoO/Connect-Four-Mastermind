
from threading import Timer
import time

import Utils
import MCTS
import Board
from Terminal import terminalAndScore
from Terminal import winningPieces


def firstTurnIsSelected(btn1, btn2, turn):
    Utils.turn = turn
    btn1.destroy()
    btn2.destroy()
    Board.createButtons()
    Board.settingHover(Utils.btnList)
    if Utils.turn == Utils.AIPiece:
        checkStateExistence()
        t = Timer(0.5, AIDropPiece) # after 0.5s ai will play --- it is just for making the game more realistic
        t.start()


# When one of 42 buttons is pushed
def userDropPiece(columnNumber) :
    # The piece must be put on the first emty cell of the selected column
    if Utils.turn == Utils.userPiece:
        notColored = [number for number in range(columnNumber, columnNumber + 6) if Utils.overallPosition[number] == 0 ]
        if len(notColored) != 0 :
            Utils.overallPosition[notColored[0]] = Utils.turn
            thisButton = Utils.btnList[notColored[0]]   # The button in which the piece should be dropped
            thisButton.config(image = Utils.imgUserPiece)
            
            finished = isGameFinished(notColored[0])
            if not finished :
                Utils.turn = Utils.AIPiece
                Board.displayLabelTurn()
                t = Timer(0.5, AIDropPiece) # after 0.5s ai will play --- it is just for making the game more realistic
                t.start()


def isGameFinished(lastPieceIndex):
    board = [piece for piece in Utils.overallPosition]
    tupleBoard = tuple(board)
    state = MCTS.State(tupleBoard)
    # If the state is in the mcts dictionary
    try:
        node = Utils.mcts[state]
        numericalAIPosition   = node.numericalAIPosition
        numericalUserPosition = node.numericalUserPosition
    # If the state is still not in the mcts dictionary
    except:
        AIPosition = ''
        userPosition = ''
        for i in range(49):
            AIPosition   += ['0', '1'][board[48 - i] == Utils.AIPiece]
            userPosition += ['0', '1'][board[48 - i] == Utils.userPiece]
        numericalAIPosition   = int(AIPosition, 2)
        numericalUserPosition = int(userPosition, 2)

    finished, winner = terminalAndScore(numericalAIPosition, numericalUserPosition)
    if finished == 1 :
        if winner == 1:
            for piece in winningPieces(lastPieceIndex, [p for p in Utils.overallPosition], Utils.turn):
                Utils.btnList[piece].config(image = Utils.imgAIPieceStar)
        if winner == -1:
            for piece in winningPieces(lastPieceIndex, [p for p in Utils.overallPosition], Utils.turn):
                Utils.btnList[piece].config(image = Utils.imgUserPieceStar)
        Utils.turn = -1
        Board.displayWinner(winner)
    return finished

def checkStateExistence():
    board = [piece for piece in Utils.overallPosition]
    tupleBoard = tuple(board)
    state = MCTS.State(tupleBoard)
    if not(state in Utils.mcts):
        if Utils.turn == Utils.AIPiece:
            node = MCTS.Node(Utils.userPiece)
        elif Utils.turn == Utils.userPiece:
            node = MCTS.Node(Utils.AIPiece)
        AIPosition = ''
        userPosition = ''
        for i in range(49):
            AIPosition   += ['0', '1'][board[48 - i] == Utils.AIPiece]
            userPosition += ['0', '1'][board[48 - i] == Utils.userPiece]
        node.numericalAIPosition   = int(AIPosition, 2)
        node.numericalUserPosition = int(userPosition, 2)
        Utils.mcts[state] = node
        return state, node
    return state, Utils.mcts[state]


def AIDropPiece():
    state, node = checkStateExistence()
    t1 = time.time()
    iterations = 0
    while(1):
        MCTS.treeTraversal(state)
        iterations += 1
        if(time.time() - t1 > 5):
            break
    # Now after doing some iterations, AI should
    #    choose the best child of the current state
    node = Utils.mcts[state]
    allChildren = [child for child in node.children]
    childrenScores = [Utils.mcts[state].totalReward/Utils.mcts[state].numVisits for state in allChildren]
    maxState = allChildren[childrenScores.index(max(childrenScores))]
    indexNewColored = indexNewPiece(Utils.overallPosition, maxState.board)
    Utils.overallPosition = [piece for piece in maxState.board]
    
    # Changing the color of the selected button
    thisButton = Utils.btnList[indexNewColored]
    thisButton.config(image = Utils.imgAIPiece)
    
    finished = isGameFinished(indexNewColored)
    if not finished :
        Utils.turn = Utils.userPiece
        Board.displayLabelTurn()
    
    
def indexNewPiece(previousState, newState):
    for i in range(len(previousState)):
        if previousState[i] != newState[i]:
            return i
    
    
    
    
    
