import unittest
import ChessBoard
import ChessLogic
import chess_utility

"""
http://pythontesting.net/framework/unittest/unittest-introduction/
"""

# TestCase for ChessBoard
class TestChessBoard(unittest.TestCase):
    def setUp(self):
        self.test_board = ChessBoard.ChessBoard()
        pass


"""
# Test case for pawn move logic:
board = cb.ChessBoard()
print(board)
board.move_piece([1,0],[2,0])
print('----------------')
print(board)

print('2,0:',logic.get_pawn_moves(board, [2,0]))
print('1,1:',logic.get_pawn_moves(board, [1,1]))

print('5,1',logic.get_pawn_moves(board, [5,1]))
board.set_piece([5,1],'Bp')
print(board)
print('5,1:',logic.get_pawn_moves(board, [5,1]))



"""





# TestCase for ChessLogic




# TestCase for utility



if __name__ == '__main__':
    unittest.main()
