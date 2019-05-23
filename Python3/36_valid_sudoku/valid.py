import unittest

class Solution:
    def stripEmpties(self, arr):
        return [c for c in arr if c != "."]
    
    def getSubSquareArr(self, board, coords):
        arr = []
        for row in board[3*coords[0]:3*coords[0]+3]:
            for c in row[3*coords[1]:3*coords[1]+3]:
                arr.append(c)
        return arr

    def getStrippedSubSquare(self, board, coords):
        return self.stripEmpties(self.getSubSquareArr(board,coords))

    def isValidArr(self, arr):
        """Given a stripped array, check to see if it contains duplicates"""
        s_arr = self.stripEmpties(arr)
        return len(s_arr) == len(set(s_arr))
    
    def isValidSudoku(self, board):
        # rows
        for row in board:
            if not self.isValidArr(row):
                return False
        # columns:
        for i in range(0,9):
            col = [r[i] for r in board]
            if not self.isValidArr(col):
                return False
        # # sub boxes
        for i in range(0,3):
            for j in range(0,3):
                coords = (i,j)
                if not self.isValidArr(self.getSubSquareArr(board, coords)):
                    return False
        return True

            
class SolTest(unittest.TestCase):
    def setUp(self):
        self.board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

        self.board_2 = [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

        self.sol = Solution()

    def test_sub_board_to_arr(self):
        arr = self.sol.getStrippedSubSquare(self.board, (0,0))
        self.assertEqual(arr, ["5", "3", "6", "9", "8"])

    def test_integration(self):
        self.assertTrue(self.sol.isValidSudoku(self.board))
        self.assertFalse(self.sol.isValidSudoku(self.board_2))        

if __name__ == "__main__":
    unittest.main()
