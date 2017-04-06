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
def translate_location():
    # TODO translate chess notation into matrix index
    pass

board = cb.ChessBoard()
"""
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
"""
logic.prompt_user_move(board)



