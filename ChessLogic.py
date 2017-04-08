import chess_utility as util

W_PAWN_START_ROW = 6
B_PAWN_START_ROW = 1

def prompt_user_move(chess_board):
    while(True):
        print(chess_board)

        # prompting user for what to move where
        while(True):
            input_move = input('what piece would you like to move? ("2,1")\n')
            piece_pos = list(map(lambda x: int(x), input_move.split(',')))

            dst = input('where should the piece go? ("4,2")\n')
            dst = list(map(lambda x: int(x), dst.split(',')))
            if is_valid_move(chess_board, piece_pos, dst):
                break
            print('Something went wrong. Try inputting correctly.')
            print(chess_board)
        print('piece_pos', piece_pos)
        piece = chess_board.piece_at(piece_pos)
        print('piece_locs1: ',chess_board.get_piece_list(piece))
        chess_board.move_piece(piece_pos, dst)
        print('piece_locs2: ',chess_board.get_piece_list(piece))

def is_valid_move(chess_board, src, dst):
    # This function needs to be efficient because
    #  we will be calling it a lot in search.
    if not (util.in_bound(src) and util.in_bound(dst)):
        return False
    if chess_board.pos_is_empty(src):
        return False

    piece = chess_board.piece_at(src)
    # TODO: First check for current check

        # TODO: Then check for current checkmate

    # Then check if move is within range of piece type
    move_range = get_legal_move_range_of_piece(chess_board,
                                               piece,
                                               src)
    print(piece, ' move range: ', move_range)
    if not (dst in move_range):
        return False

    # you cannot take your own piece
    if chess_board.compare_color(src, dst) == 0:
        return False
    return True

    # Then check if moving causes home king to check

def get_legal_move_range_of_piece(board, piece, pos):
    # This should be really light weight.
    # legal move or just any move?

    if piece[1] == 'p':
        return get_pawn_moves(board, pos)
    elif piece[1] == 'K':
        return get_king_moves(board, pos)
    elif piece[1] == 'q':
        return get_queen_moves(board, pos)
    elif piece[1] == 'k':
        return get_knight_moves(board, pos)
    elif piece[1] == 'r':
        return get_rook_moves(board, pos)
    elif piece[1] == 'b':
        return get_bishop_moves(board, pos)


def is_check(chess_board, king_pos):
    # go through opponent moves and see if king_pos

    pass

def get_list_of_all_moves(chess_board, color):
    # This function should just call get_move_range on all pieces.
    pass

def get_pawn_moves(board, pawn_pos):
    # generate all possible moves
    # it can move forward, left or right.
    moves = []
    if (board.piece_at(pawn_pos) != 'Bp' and
        board.piece_at(pawn_pos) != 'Wp'):
        # TODO: throw some kind of error.
        print('PAWN NOT FOUND AT {}. NO MOVES.'
              .format(pawn_pos))
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
        print('KING NOT FOUND AT {}. NO MOVES'
              .format(king_pos))
        return moves
    n = util.calc_pos(king_pos, -1, 0)
    e = util.calc_pos(king_pos, 0, 1)
    s = util.calc_pos(king_pos, 1, 0)
    w = util.calc_pos(king_pos, 0, -1)

    ne = util.calc_pos(king_pos, -1, 1)
    se = util.calc_pos(king_pos, 1, 1)
    sw = util.calc_pos(king_pos, 1, -1)
    nw = util.calc_pos(king_pos, -1, -1)

    add_move_helper(board, king_pos, moves, n)
    add_move_helper(board, king_pos, moves, e)
    add_move_helper(board, king_pos, moves, s)
    add_move_helper(board, king_pos, moves, w)
    add_move_helper(board, king_pos, moves, ne)
    add_move_helper(board, king_pos, moves, se)
    add_move_helper(board, king_pos, moves, sw)
    add_move_helper(board, king_pos, moves, nw)

    return moves

def add_move_helper(board, king_pos, moves, move):
    if (util.in_bound(move) and
        board.compare_color(king_pos, move)!=0):
        moves.append(move)

def get_knight_moves(board, k_pos):
    moves = []
    if (board.piece_at(k_pos) != 'Wk' and
        board.piece_at(k_pos) != 'Bk'):
        print('KNIGHT NOT FOUND AT {}. NO MOVES'
              .format(k_pos))
        return moves

    nne = util.calc_pos(k_pos, -2, 1)
    nee = util.calc_pos(k_pos, -1, 2)
    see = util.calc_pos(k_pos, 1, 2)
    sse = util.calc_pos(k_pos, 2, 1)
    ssw = util.calc_pos(k_pos, 2, -1)
    sww = util.calc_pos(k_pos, 1, -2)
    nww = util.calc_pos(k_pos, -1, -2)
    nnw = util.calc_pos(k_pos, -2, -1)

    add_move_helper(board, k_pos, moves, nne)
    add_move_helper(board, k_pos, moves, nee)
    add_move_helper(board, k_pos, moves, see)
    add_move_helper(board, k_pos, moves, sse)
    add_move_helper(board, k_pos, moves, ssw)
    add_move_helper(board, k_pos, moves, sww)
    add_move_helper(board, k_pos, moves, nww)
    add_move_helper(board, k_pos, moves, nnw)
    return moves

def get_bishop_moves(board, b_pos):
    moves = []
    if (board.piece_at(b_pos) != 'Wb' and
        board.piece_at(b_pos) != 'Bb'):
        print('BISHOP NOT FOUND AT {}. NO MOVES'
              .format(b_pos))
        return moves

    direction_move_helper(board, b_pos, moves, [1,1])
    direction_move_helper(board, b_pos, moves, [1,-1])
    direction_move_helper(board, b_pos, moves, [-1,1])
    direction_move_helper(board, b_pos, moves, [-1,-1])
    return moves

def get_rook_moves(board, r_pos):
    moves = []

    if (board.piece_at(r_pos) != 'Wr' and
        board.piece_at(r_pos) != 'Br'):
        print('ROOK NOT FOUND AT {}. NO MOVES'
              .format(r_pos))
        return moves

    direction_move_helper(board, r_pos, moves, [1,0])
    direction_move_helper(board, r_pos, moves, [-1,0])
    direction_move_helper(board, r_pos, moves, [0,1])
    direction_move_helper(board, r_pos, moves, [0,-1])
    return moves

def get_queen_moves(board, q_pos):
    moves = []

    if (board.piece_at(q_pos) != 'Wq' and
        board.piece_at(q_pos) != 'Bq'):
        print('QUEEN NOT FOUND AT {}. NO MOVES.'
              .format(q_pos))
        return moves
    # go all 8 directions and keep adding moves until you
    #   capture an enemy
    #   reach the boundary
    #   are blocked by allied piece

    direction_move_helper(board, q_pos, moves, [1,1])
    direction_move_helper(board, q_pos, moves, [1,0])
    direction_move_helper(board, q_pos, moves, [1,-1])
    direction_move_helper(board, q_pos, moves, [0,1])
    direction_move_helper(board, q_pos, moves, [0,-1])
    direction_move_helper(board, q_pos, moves, [-1,1])
    direction_move_helper(board, q_pos, moves, [-1,0])
    direction_move_helper(board, q_pos, moves, [-1,-1])
    return moves

def direction_move_helper(board, q_pos, moves, direction):
    next_move = util.calc_pos(q_pos, direction[0], direction[1])
    while(True):
        # if next_move is empty space. add it to the list
        if not util.in_bound(next_move):
            break
        # the space is empty and we can keep adding moves
        if board.pos_is_empty(next_move):
            moves.append(next_move)
        elif board.compare_color(q_pos, next_move) == 1:
            moves.append(next_move)
            break
        elif board.compare_color(q_pos, next_move) == 0:
            break
        next_move = util.calc_pos(next_move,
                                  direction[0],
                                  direction[1])


