import ChessBoard as cb
import ChessLogic as logic

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

INDEX_PIECE_MAP = {
    0:'',
    1:'p',
    2:'k',
    3:'b',
    4:'r',
    5:'q',
    6:'K'
}

PIECE_INDEX_MAP = {
    '':0,
    'p':1,
    'k':2,
    'b':3,
    'r':4,
    'q':5,
    'K':6
}

def translate_location():
    # TODO translate chess notation into matrix index
    pass

def check_valid_move(board, src, dst):
    # check if out of bounds
    if (src[0] < 0 or src[0] > 7 or
        src[1] < 0 or src[0] > 7 or
        dst[0] < 0 or dst[0] > 7 or
        dst[1] < 0 or dst[1] > 7):
        return False
    # check if there is no piece
    if board[src[0]][src[1]] == '':
        return False

    return True

board = cb.ChessBoard()
print(board)
board.move_piece([1,0],[2,0])
print('----------------')
print(board)

print('2,0:',logic.get_pawn_moves(board, [2,0]))
print('1,1:',logic.get_pawn_moves(board, [1,1]))

print('5,1',logic.get_pawn_moves(board, [5,1]))
board.add_piece([5,1],'Bp')
print(board)
print('5,1:',logic.get_pawn_moves(board, [5,1]))


