BLACK = 'B'
WHITE = 'W'
EMPTY_SPACE = ''
def is_piece_black(piece):
    return piece[0] == BLACK
def is_piece_white(piece):
    return piece[0] == WHITE
def is_piece(piece):
    return piece != EMPTY_SPACE
