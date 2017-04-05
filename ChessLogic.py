import chess_utility as util

def is_valid_move(chess_board, src, dst):
    # This function needs to be efficient because
    #  we will be calling it a lot in search.

    # First check for current check

        # Then check for current checkmate

    # Check if dst is a piece being taken
    # Make sure it not home piece.

    # Then check if move is within range of piece type

    # Then check if moving causes home king to check

def get_legal_move_range_of_piece():
    # This should be really light weight.
    # legal move or just any move?

def is_check(chess_board, king_pos):
    # This function should also be light weight.

def get_list_of_available_moves(chess_board, color):
    # This function should just call get_move_range on all pieces.

def get_pawn_moves(board, pawn_pos):
    # generate all possible moves
    # it can move forward, left or right.
    moves = []

    if board.pos_is_white_piece(pawn_pos):

    else if: board.pos_is_black_piece(pawn_pos):



    # remove illegal ones

    # return a list of possible moves.
    pass

def get_king_moves():
    pass

def get_knight_moves():
    pass

def get_rook_moves():
    pass

def get_queen_moves():
    pass

def get_bishop_moves():
    pass

