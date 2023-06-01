
userPiece = 1
AIPiece   = 2

c = 2 ** 0.5   # Exploration constant in ucb

numSimulations = 1   # Number of simulations in each rolling out

btnList = {}   # The (index -> tkinter buttons) pair

overallPosition = [0] * 49
# The indices are :
# Gaurd --- 6 | 13 | 20 | 27 | 34 | 41 | 48
#           -------------------------------
#    ---    5 | 12 | 19 | 26 | 33 | 40 | 47
#    ---    4 | 11 | 18 | 25 | 32 | 39 | 46
#    ---    3 | 10 | 17 | 24 | 31 | 38 | 45
#    ---    2 | 9  | 16 | 23 | 30 | 37 | 44
#    ---    1 | 8  | 15 | 22 | 29 | 36 | 43
#    ---    0 | 7  | 14 | 21 | 28 | 35 | 42


currentNumericalAIPosition   = 0   # based on binary position of AI pieces
currentNumericalUserPosition = 0   # based on binary position of User pieces


# We use a dictionary to store the nodes
# of the MCTS
# key -> value is :   State (hash value of state) -> Node
mcts = {}

imgAIPiece = None
imgUserPiece = None
imgAIPieceStar = None
imgUserPieceStar = None

turn = -1          # Whose turn is it?

lblTurn = None       # User(green)   AI(red)
lblWinner = None     # Label for announcing the winner
