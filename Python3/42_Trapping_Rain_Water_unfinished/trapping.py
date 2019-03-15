import unittest

class Solution:
    def trap(self, height: 'List[int]') -> int:
        lower = 0
        upper = 1

        total_area = 0
        curr_area = 0

        while upper < len(height):
            while height[upper] < height[lower]:
                curr_area += (height[lower] - height[upper])

        total_area += curr_area

class TestSol(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_first(self):
        h = [0,1,0,2,1,0,1,3,2,1,2,1]
        
        self.assertEqual(self.sol.trap(h), 6)



if __name__ == "__main__":
    unittest.main()
