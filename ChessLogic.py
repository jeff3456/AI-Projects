import chess_utility as util

W_PAWN_START_ROW = 6
B_PAWN_START_ROW = 1

def is_valid_move(chess_board, src, dst):
    # This function needs to be efficient because
    #  we will be calling it a lot in search.

    # First check for current check

        # Then check for current checkmate

    # Check if dst is a piece being taken
    # Make sure it not home piece.

    # Then check if move is within range of piece type

    # Then check if moving causes home king to check
    pass

def get_legal_move_range_of_piece():
    # This should be really light weight.
    # legal move or just any move?
    pass

def is_check(chess_board, king_pos):
    # This function should also be light weight.
    pass

def get_list_of_available_moves(chess_board, color):
    # This function should just call get_move_range on all pieces.
    pass

def get_pawn_moves(board, pawn_pos):
    # generate all possible moves
    # it can move forward, left or right.
    moves = []
    if (board.piece_at(pawn_pos) != 'Bp' and
        board.piece_at(pawn_pos) != 'Wp'):
        # TODO: throw some kind of error.
        print("PAWN NOT FOUND. NO MOVES.")
        return moves

    # I dont want to repeat code so set variables here.
    if board.pos_is_white_piece(pawn_pos):
        direction = -1
        start_row = W_PAWN_START_ROW
    else:
        direction = 1
        start_row = B_PAWN_START_ROW

    # Check if diags are okay first
    left_diag = util.calc_pos(pawn_pos, direction, -1)
    right_diag = util.calc_pos(pawn_pos, direction, 1)
    one_forward = util.calc_pos(pawn_pos, direction, 0)
    two_forward = util.calc_pos(pawn_pos, 2*direction, 0)
    if (util.in_bound(left_diag) and
        board.compare_color(left_diag, pawn_pos) == 1):
        moves.append(left_diag)
    if (util.in_bound(right_diag) and
        board.compare_color(right_diag, pawn_pos) == 1):
        moves.append(right_diag)
    if (util.in_bound(one_forward) and
        board.pos_is_empty(one_forward)):
        moves.append(one_forward)
    if (util.in_bound(two_forward) and
        board.pos_is_empty(two_forward) and
        pawn_pos[0] == start_row):
        moves.append(two_forward)
    return moves

def get_king_moves(board, king_pos):
    moves = []
    # one space all 8 directions.
    # make sure in bounds and not home piece.
    if (board.piece_at(king_pos) != 'BK' and
        board.piece_at(king_pos) != 'WK'):
        # TODO: throw some kind of error.
        print("KING NOT FOUND. NO MOVES")
        return moves
    n = util.calc_pos(king_pos, -1, 0)
    e = util.calc_pos(king_pos, 0, 1)
    s = util.calc_pos(king_pos, 1, 0)
    w = util.calc_pos(king_pos, 0, -1)

    ne = util.calc_pos(king_pos, -1, 1)
    se = util.calc_pos(king_pos, 1, 1)
    sw = util.calc_pos(king_pos, 1, -1)
    nw = util.calc_pos(king_pos, -1, -1)



    pass

def get_knight_moves():
    pass

def get_rook_moves():
    pass

def get_queen_moves():
    pass

def get_bishop_moves():
    pass

