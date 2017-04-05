BLACK = 'B'
WHITE = 'W'
EMPTY_SPACE = ''
def is_piece_black(piece):
    if piece == EMPTY_SPACE:
        return False
    return piece[0] == BLACK
def is_piece_white(piece):
    if piece == EMPTY_SPACE:
        return False
    return piece[0] == WHITE
def is_empty(piece):
    return piece == EMPTY_SPACE
def is_piece(piece):
    return piece != EMPTY_SPACE

def in_bound(pos):
    return not (pos[0] < 0 or pos[0] > 7 or
                pos[1] < 0 or pos[1] > 7)
def calc_pos(pos, row_change, col_change):
    return [pos[0]+row_change, pos[1]+col_change]
