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

class ChessBoard:
    """
    CheckBoard stores the relevant data of the current state of 
    ChessBoard and related methods that change or check that data.
    """

    def __init__(self, set_up=True):
        self.board = _create_board()
        if(set_up):
            _set_up_game(self.board)
            # Create dictionary for each type 
            self.white = {}
            self.black = {}

            self.white['Wp'] = []
            self.black['Bp'] = []
            for col in range(8):
                self.black['Bp'].append([1,col])
                self.white['Wp'].append([6,col])

            self.black['Bk'] = [[0,1],[0,6]]
            self.black['Bb'] = [[0,2],[0,5]]
            self.black['Br'] = [[0,0],[0,7]]
            self.black['Bq'] = [[0,3]]
            self.black['Bk'] = [[0,4]]

            self.white['Wk'] = [[7,1],[7,6]]
            self.white['Wb'] = [[7,2],[7,5]]
            self.white['Wr'] = [[7,0],[7,7]]
            self.white['Wq'] = [[7,3]]
            self.white['Wk'] = [[7,4]]

    def __str__(self):
        output_str = ''
        for row in self.board:
            for i in range(8):
                if row[i] == '':
                    output_str = output_str + ' '
                else:
                    output_str = output_str + PIECE_UNICODE_MAP[row[i]]
            output_str = output_str + '\n'
        return output_str

    def __repr__(self):
        return self.__str__()

    def move_piece(self, src, dst):
        
        if self.board[dst[0]][dst[1]] != '':
            # remove that piece from the list
            self.remove(dst)
        temp = self.board[src[0]][src[1]]
        self.board[src[0]][src[1]] = ''
        self.board[dst[0]][dst[1]] = temp

    def remove(self, dst):
        piece = self.board[dst[0]][dst[1]]
        # find white or black piece list
        if piece[0] == 'W':
            piece_list = self.white[piece]
        else:
            piece_list = self.black[piece]
        piece_list.remove([dst[0], dst[1]])
        self.board[dst[0]][dst[1]] = ''

def _create_board():
    board = []
    row = []
    for i in range(8):
        row.append('')
    for i in range(8):
        board.append(row.copy())
    return board

def _set_up_game(board):
    for i in range(8):
        board[1][i] = 'Bp'
        board[6][i] = 'Wp'
    black_row = ['Br','Bk','Bb','Bq','BK','Bb','Bk','Br']
    white_row = ['Wr','Wk','Wb','Wq','WK','Wb','Wk','Wr']
    board[0] = black_row
    board[7] = white_row
