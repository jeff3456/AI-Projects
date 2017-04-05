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
PIECE_UNICODE_MAP = {
    'Bp':'\u265F',
    'Bk':'\u265E',
    'Bb':'\u265D',
    'Br':'\u265C',
    'Bq':'\u265B',
    'BK':'\u265A',
    'Wp':'\u2659',
    'Wk':'\u2658',
    'Wb':'\u2657',
    'Wr':'\u2656',
    'Wq':'\u2655',
    'WK':'\u2654'
}

def translate_location():
    pass

def make_board():
    board = []
    row = []
    for i in range(8):
        row.append('')
    for i in range(8):
        board.append(row.copy())
    return board

def set_up_game(board):
    for i in range(8):
        board[1][i] = 'Bp'
        board[6][i] = 'Wp'
    black_row = ['Br','Bk','Bb','Bq','BK','Bb','Bk','Br']
    white_row = ['Wr','Wk','Wb','Wq','WK','Wb','Wk','Wr']
    board[0] = black_row
    board[7] = white_row
    return board

def print_board(board):
    for row in board:
        for i in range(8):
            if row[i] == '':
                print(' ', end='')
            else:
                print(PIECE_UNICODE_MAP[row[i]], end='')
        print('')

board = make_board()
set_up_game(board)
print_board(board)
