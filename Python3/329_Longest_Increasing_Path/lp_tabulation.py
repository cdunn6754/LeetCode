import unittest

class Solution:
    def  __init__(self, nums = None):
        self.neighbors = {}
        self.memo_paths = {}

        if not nums == None:
            self.nums = nums

    def eval_nums(self, loc):
        return self.nums[loc[0]][loc[1]]

    def get_linear_idx(self, loc):
        return len(self.nums[0]) * loc[0] + loc[1]

    def get_matrix_idx(self, lin_idx):
        return (lin_idx // len(self.nums[0]), lin_idx % len(self.nums[0]))
        
    def find_viable_neighbors(self, loc):
        if loc in self.neighbors:
            return self.neighbors[loc]

        ns = set()
        if loc[0] > 0 and self.eval_nums(loc) < self.eval_nums((loc[0] - 1, loc[1])):
            ns.add((loc[0] - 1, loc[1]))
        if loc[1] > 0and self.eval_nums(loc) < self.eval_nums((loc[0], loc[1] - 1)):
            ns.add((loc[0], loc[1] - 1))
        if (loc[0]+1 < len(self.nums) and
            self.eval_nums(loc) < self.eval_nums((loc[0] + 1, loc[1]))):
            ns.add((loc[0] + 1, loc[1]))
        if (loc[1]+1 < len(self.nums[0])
            and self.eval_nums(loc) < self.eval_nums((loc[0], loc[1] + 1))):
            ns.add((loc[0], loc[1] + 1))

        return ns
        
    def longestIncreasingPath(self, matrix) -> int:
        self.nums = matrix

        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        L = m * n
        prev_paths = [1] * L
        curr_paths = [1] * L


        for _ in range(0,L):
            for lin_idx in range(0,L):
                neis = self.find_viable_neighbors(self.get_matrix_idx(lin_idx))
                if len(neis) > 0:
                    curr_paths[lin_idx] = 1 + max(
                        [prev_paths[self.get_linear_idx(i)] for
                         i in neis])
            prev_paths = curr_paths
        return max(curr_paths)
                
        


class TestItUp(unittest.TestCase):
    def setUp(self):
        self.nums = [
            [9,9,4],
            [6,6,8],
            [2,1,1]
        ]
        self.nums_2 = [
            [3,4,5],
            [3,2,6],
            [2,2,1]            
        ]
        self.nums_simple = [
            [1,4],
            [2,3]
        ]

        self.sol = Solution()
    
    def test_1(self):
        self.assertEqual(self.sol.longestIncreasingPath(self.nums), 4)

    def test_2(self):
        self.assertEqual(self.sol.longestIncreasingPath(self.nums_2), 4)

    def test_3(self):
        self.assertEqual(self.sol.longestIncreasingPath(self.nums_simple), 4)


unittest.main()
