import random
from math import log, sqrt, inf
import Utils
from Terminal import terminalAndScore


class State:
    def __init__(self, board):
        self.board = board     # board is a 2D tuple

    def __hash__(self):
        return hash(self.board)

    def __eq__(self, other):
        return self.board == other.board
    
    def __str__(self):
        strBoard = ""
        for row in range(5, -1, -1):
            for col in range(7):
                strBoard += str(self.board[row + 7 * col])
                strBoard += " "
            strBoard += "\n"
        return strBoard


# Each node in the Monte Carlo Tree Search
# has these attributes
class Node:
    def __init__(self, turn):
        self.turn        = turn          # The node was created in the turn of the AI or player
                                         #   (AI or player dropped the piece to create the state)
                                   
        self.numericalAIPosition = 0     # an integer to represent the AI position
        self.numericalUserPosition = 0   # an integer to represent the User position
        self.children = []               # The children includes instances of the State class
        self.allParents = {}             # Since a state can be reached through different paths, it may have more than one parent state.
                                         #    Dictionary of all parent states {parentState -> propagatedReward, propagatedVisits}
        self.isTerminal = 0              # Is it a terminal state?
        self.totalReward = 0
        self.numVisits   = 0
        
    def addChild(self, childState):
        self.children.append(childState)
    

    def addParent(self, parentState, rewardChild, visitsChild):
        self.allParents[parentState] = (rewardChild, visitsChild)



## --------------- MCTS Algorithm Begins --------------- ##

# Phase 1 ---> Tree Traversal (Selection)
# Phase 2 ---> Node Expansion
def treeTraversal(state):
    node = Utils.mcts[state]
    # This state is a terminal state, so no need to traverse this state
    if node.isTerminal:
        return
    
    Utils.currentNumericalAIPosition   = node.numericalAIPosition
    Utils.currentNumericalUserPosition = node.numericalUserPosition
    
    # Check if the state is a leaf node
    #   i.e., it is not terminal (yet), but also
    #   it has no children
    leaf = len(node.children) == 0
    
  
    # If it is not a leaf node, chooses a child node
    #   that maximizes the UCB score
    while not(leaf):
        state, node = maximizeUCB(node)
        leaf = len(node.children) == 0
    
    
    # If this node has not been visited yet, simulates it
    if node.numVisits == 0:
        reward = rollOut(state, node)   # If a node is a terminal node, inside the rollout it is clarified
        node.numVisits   += Utils.numSimulations
        node.totalReward += reward
        backpropagation(state, node)
    
    
    # If this node has been visited already, expands it (or if it is a terminal node, backpropagates only)
    else:
        if not node.isTerminal:
            # We expand the node here
            isAnyChildAlreadyExpanded = createChildStates(state, node)       # Adding new (state -> node) to the mcts dictionary
            # If any child has already been in the mcts dictionary,
            #    we just backpropagate its statistics and don't
            #    simulate any other children
            if not isAnyChildAlreadyExpanded:
                state = random.choice(node.children)
                node = Utils.mcts[state]
                reward = rollOut(state, node)   # If a node is a terminal node, inside rollout it is clarified
                node.numVisits   += Utils.numSimulations
                node.totalReward += reward
                backpropagation(state, node)
                
        elif node.isTerminal:
                reward = rollOut(state, node)   # If a node is a terminal node, inside rollout it is clarified
                node.numVisits   += Utils.numSimulations
                node.totalReward += reward
                backpropagation(state, node)

def legalMoves(board):
    indexLegalCells = []
    for i in range(7) :  # in each iteration, we try to put a piece on a single column
        freeCellIndex = -1   # The column has not an empty cell
        if board[i * 7 + 0] == 0 :
            freeCellIndex = i * 7 + 0
        elif board[i * 7 + 1] == 0 :
            freeCellIndex = i * 7 + 1
        elif board[i * 7 + 2] == 0 :
            freeCellIndex = i * 7 + 2
        elif board[i * 7 + 3] == 0 :
            freeCellIndex = i * 7 + 3
        elif board[i * 7 + 4] == 0 :
            freeCellIndex = i * 7 + 4
        elif board[i * 7 + 5] == 0 :
            freeCellIndex = i * 7 + 5
        
        if freeCellIndex != -1:   # We have at least an empty column to put the piece
            indexLegalCells.append(freeCellIndex)
    return indexLegalCells


# Considers all possible actions in a state
#    and creates the children of that state.
# If there is a child that has already been expanded,
#    backpropagates the result of that child, and returns 1.
def createChildStates(state, node) :
    isAnyChildAlreadyExpanded = 0
    indexLegalCells = legalMoves(state.board)
    childrenAlreadyExists = []
    if node.turn == Utils.AIPiece:
        childTurn = Utils.userPiece
    else:
        childTurn = Utils.AIPiece
    for index in indexLegalCells :  # in each iteration, we try to put a piece on a single column
        newBoard = [piece for piece in state.board]
        newBoard[index] = childTurn
        tupleNewBoard = tuple(newBoard)
        flag, childState, childNode = createOneChild(state, node, tupleNewBoard, childTurn, index)
        if flag:
            isAnyChildAlreadyExpanded = 1
            childrenAlreadyExists.append((childState, childNode))
    for childState, childNode in childrenAlreadyExists:
        backpropagation(childState, childNode)
    return isAnyChildAlreadyExpanded


def createOneChild(parentState, parentNode, childBoard, childTurn, newPieceIndex):
    childState = State(childBoard)
    parentNode.addChild(childState)
    flag = 0
    if not(childState in Utils.mcts):   # If the childState (child board) is not in the mcts, creates and adds it to the mcts dictionary
        childNode  = Node(childTurn)
        if childTurn == Utils.AIPiece:
            childNode.numericalAIPosition   = parentNode.numericalAIPosition | (1 << newPieceIndex)
            childNode.numericalUserPosition = parentNode.numericalUserPosition
        elif childTurn == Utils.userPiece:
            childNode.numericalAIPosition   = parentNode.numericalAIPosition
            childNode.numericalUserPosition = parentNode.numericalUserPosition | (1 << newPieceIndex)
        childNode.addParent(parentState, 0, 0)
        Utils.mcts[childState] = childNode
        
    else:    # If the childState (child board) is in the mcts, just appends the current state to the child node parents
        childNode  = Utils.mcts[childState]
        childNode.addParent(parentState, 0, 0)
        flag = 1
    return flag, childState, childNode



# Phase 3 ---> Rollout
def rollOut(state, node):
    numericalAIPosition   = node.numericalAIPosition
    numericalUserPosition = node.numericalUserPosition
    
    # This is for detecting terminal states, so that
    #    we don't expand their children
    finished, _ = terminalAndScore(numericalAIPosition, numericalUserPosition)
    if finished:
        node.isTerminal = 1
        
    totalScore = 0
    for i in range(Utils.numSimulations):
        board = [piece for piece in state.board]
        childTurn = node.turn
        while True:
            finished, winner = terminalAndScore(numericalAIPosition, numericalUserPosition)
            if finished == 1:   # This state (board position) is a terminal state
                totalScore += winner
                break
            
            indexLegalCells = legalMoves(board)
            action = random.choice(indexLegalCells)
            
            if childTurn == Utils.AIPiece:
                childTurn = Utils.userPiece
                numericalUserPosition |= (1 << action)
            else:
                childTurn = Utils.AIPiece
                numericalAIPosition   |= (1 << action)
            board[action] = childTurn
    
    return totalScore
        
        
# Phase 4 ---> Backpropagation
# allParent = dict{parentState -> propagatedReward, propagatedVisits}
def backpropagation(state, node):    
    for parentState in node.allParents:
        # The propagatedYYYY are the values of a node's statistics which were backpropagated to a specific parent
        propagatedReward, propagatedVisits = node.allParents[parentState]
        # The currentYYYY are the current values of a node's statistics
        currentReward, currentVisits = node.totalReward, node.numVisits
        
        parentNode = Utils.mcts[parentState]
        
        # If the parent can't be reached through current board position
        #    it is not accessible and we don't need to update it anymore
        isParentAccessible = Utils.currentNumericalAIPosition & parentNode.numericalAIPosition == Utils.currentNumericalAIPosition
        isParentAccessible &= Utils.currentNumericalUserPosition & parentNode.numericalUserPosition == Utils.currentNumericalUserPosition
        inconsistency = (propagatedReward != currentReward) or (propagatedVisits != currentVisits)
        
        # If a parent is accessible and there are inconsitencies between
        #    propagated values and current values, we should update values
        if isParentAccessible and inconsistency:
            node.allParents[parentState]  = (currentReward, currentVisits)
            parentNode.totalReward = parentNode.totalReward - propagatedReward + currentReward
            parentNode.numVisits   = parentNode.numVisits - propagatedVisits + currentVisits
            
            backpropagation(parentState, parentNode)
   



def maximizeUCB(node):
    childrenStatesList = node.children
    
    maxUCB = -inf
    for state in childrenStatesList:
        tmpChildNode = Utils.mcts[state]
        tmpUCB = ucb(node, tmpChildNode)
        if tmpUCB > maxUCB:
            maxChildState = state
            maxChildNode = tmpChildNode
            maxUCB = tmpUCB
    return maxChildState, maxChildNode
    
    
def ucb(node, childNode):
    if childNode.numVisits == 0:
        return inf
    if childNode.turn == Utils.AIPiece:
        exploitation = childNode.totalReward / childNode.numVisits
    elif childNode.turn == Utils.userPiece:
        exploitation = -childNode.totalReward / childNode.numVisits
    exploration  = sqrt(log(node.numVisits)/childNode.numVisits)
    return exploitation + Utils.c * exploration




