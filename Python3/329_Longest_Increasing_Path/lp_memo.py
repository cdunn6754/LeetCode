import unittest

class Solution:
    def  __init__(self, nums = None):
        self.neighbors = {}
        self.memo_paths = {}

        if not nums == None:
            self.nums = nums

    def eval_nums(self, loc):
        return self.nums[loc[0]][loc[1]]
        
    def find_neighbors(self, loc):
        if loc in self.neighbors:
            return self.neighbors[loc]

        ns = set()
        if loc[0] > 0:
            ns.add((loc[0] - 1, loc[1]))
        if loc[1] > 0:
            ns.add((loc[0], loc[1] - 1))
        if loc[0]+1 < len(self.nums):
            ns.add((loc[0] + 1, loc[1]))
        if loc[1]+1 < len(self.nums[0]):
            ns.add((loc[0], loc[1] + 1))

        return ns
    def r_get_longest_path(self, loc):

        if not self.memo_paths.get(loc) == None:
            return self.memo_paths[loc] + 1
        
        viable_ns = [n for n in self.find_neighbors(loc)
                     if self.eval_nums(loc) < self.eval_nums(n)]

        if len(viable_ns) == 0:
            return 1

        max_len = 0
        for n in viable_ns:
            curr_len = self.r_get_longest_path(n)
            max_len = curr_len if curr_len > max_len else max_len

        self.memo_paths[loc] = max_len
        return max_len + 1
        
    def longestIncreasingPath(self, matrix) -> int:
        self.nums = matrix

        max_len = 0

        for r_idx, row in enumerate(matrix):
            for e_idx, e in enumerate(row):
                curr_len = self.r_get_longest_path((r_idx, e_idx))
                max_len = curr_len if curr_len > max_len else max_len
        return max_len
                
        


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

        self.sol = Solution()

    def test_recursive_long_path(self):
        sol = Solution(self.nums)
        
        self.assertEqual(sol.r_get_longest_path((2,0)), 3)
    
    def test_1(self):
        self.assertEqual(self.sol.longestIncreasingPath(self.nums), 4)

    def test_2(self):
        self.assertEqual(self.sol.longestIncreasingPath(self.nums_2), 4)


unittest.main()
