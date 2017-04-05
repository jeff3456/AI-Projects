def is_valid_move(chess_board, src, dst):
    # This function needs to be efficient because
    #  we will be calling it a lot in search.

    # First check for current check

        # Then check for current checkmate

    # Check if dst is a piece being taken
    # Make sure it not home piece.

    # Then check if move is within range of piece type

    # Then check if moving causes home king to check

def get_move_range():
    # This should be really light weight.


def is_check(chess_board, src):
    # This function should also be light weight.

def get_list_of_available_moves(chess_board, color):
    # This function should just call get_move_range on all pieces.

