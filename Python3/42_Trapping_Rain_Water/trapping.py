import unittest

class Solution:
    def trap(self, height: 'List[int]') -> int:
        if len(height) == 0:
            return 0

        left_max= [None]*len(height)
        right_max = [None]*len(height)

        water_depth = 0

        max_h = height[0]
        for idx, _ in enumerate(left_max):
            if height[idx] > max_h:
                max_h = height[idx]
            left_max[idx] = max_h

        max_h = height[-1]
        for idx in reversed(range(len(height))):
            if height[idx] > max_h:
                max_h = height[idx]
            right_max[idx] = max_h

        for idx, h in enumerate(height):
            water_depth += min(left_max[idx], right_max[idx]) - h

        return water_depth

        
            
                

class TestSol(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_first(self):
        h = [0,1,0,2,1,0,1,3,2,1,2,1]
        
        self.assertEqual(self.sol.trap(h), 6)



if __name__ == "__main__":
    unittest.main()
