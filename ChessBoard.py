import chess_utility as util

PIECE_UNICODE_MAP = {
    'Wp':'\u265F',
    'Wk':'\u265E',
    'Wb':'\u265D',
    'Wr':'\u265C',
    'Wq':'\u265B',
    'WK':'\u265A',
    'Bp':'\u2659',
    'Bk':'\u2658',
    'Bb':'\u2657',
    'Br':'\u2656',
    'Bq':'\u2655',
    'BK':'\u2654'
}

EMPTY_SPACE = ''

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
        # TODO: create build string function and separate it
        output_str = ''
        for row in self.board:
            for i in range(8):
                if row[i] == '':
                    output_str = output_str + ' '
                else:
                    output_str = (output_str +
                                  PIECE_UNICODE_MAP[row[i]])
            output_str = output_str + '\n'
        return output_str

    def __repr__(self):
        return self.__str__()

    def move_piece(self, src, dst):
        if util.is_piece(self.piece_at(dst)):
            # remove that piece from the list
            self.remove(dst)
        temp = self.piece_at(src)
        self.set_piece(src, '')
        self.set_piece(dst, temp)

    def remove(self, dst):
        piece = self.piece_at(dst)
        if piece == EMPTY_SPACE:
            return
        # find white or black piece list
        if util.is_piece_white(piece):
            piece_list = self.get_piece_list(piece)
        else:
            piece_list = self.get_piece_list(piece)
        piece_list.remove([dst[0], dst[1]])
        self.set_piece(dst, EMPTY_SPACE)

    def add_piece(self, pos, piece):
        """ USE THIS TO ADD A PIECE TO THE GAME"""
        self.set_piece(pos, piece)
        p_list = self.get_piece_list(piece)
        p_list.append(pos)

    def set_piece(self, pos, piece):
        """ THIS ONLY ADD PIECE TO MATRIX REPRESENTATION
        """
        self.board[pos[0]][pos[1]] = piece
    def piece_at(self, pos):
        return self.board[pos[0]][pos[1]]
    def get_piece_list(self, piece):
        if util.is_piece_white(piece):
            return self.white[piece]
        elif util.is_piece_black(piece):
            return self.black[piece]
        return None
    def pos_is_white_piece(self, pos):
        return util.is_piece_white(self.piece_at(pos))
    def pos_is_black_piece(self, pos):
        return util.is_piece_black(self.piece_at(pos))
    def pos_is_empty(self, pos):
        return util.is_empty(self.piece_at(pos))
    def compare_color(self, pos1, pos2):
        if (self.pos_is_white_piece(pos1) and
            self.pos_is_white_piece(pos2)):
            return 0
        if (self.pos_is_black_piece(pos1) and
            self.pos_is_black_piece(pos2)):
            return 0
        if (self.pos_is_empty(pos1) or self.pos_is_empty(pos2)):
            return -1
        return 1

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
