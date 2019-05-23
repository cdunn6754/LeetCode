import unittest

class Solution:
    def valid_move(self, idx):
        if idx in self.known:
            return False
        if idx[0] < 0 or idx[0] >= self.row_length:
            return False
        if idx[1] < 0 or idx[1] >= self.col_length:
            return False
        return True

    def get_next_move(self, idx):
        
        move_priority = [
            lambda idx: (idx[0], idx[1]+1),
            lambda idx: (idx[0]+1, idx[1]),
            lambda idx: (idx[0], idx[1]-1),
            lambda idx: (idx[0]-1, idx[1])
            ]

        if self.valid_move(self.curr_move(idx)):
            return self.curr_move(idx)

        for move in move_priority:
            if self.valid_move(move(idx)):
                self.curr_move = move
                return move(idx)

        return False
        
    def spiralOrder(self, matrix):
        self.known = set()
        self.curr_move = lambda idx: (idx[0], idx[1]+1)
        result = []

        self.row_length = len(matrix)
        self.col_length = len(matrix[0])

        idx = (0,0)
        while idx:
            print(idx, matrix[idx[0]][idx[1]])
            result.append(matrix[idx[0]][idx[1]])
            self.known.add(idx)
            idx = self.get_next_move(idx)

        return result            
             

class Testy(unittest.TestCase):

    def test_1(self):
        mat = [
            [ 1, 2, 3, 4, 5],
            [ 6, 7, 8, 9, 10],
            [ 11, 12, 13, 14, 15],
            [ 16, 17, 18, 19, 20]
        ]

        print("hiya buddy", mat[0][1])
        sol = Solution()
        
        self.assertEqual(sol.spiralOrder(mat),
                         [1,2,3,4,5,10,15,20,19,18,17,16,11,6,7,8,9,14,13,12])

unittest.main()
