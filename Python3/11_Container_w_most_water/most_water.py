import unittest
class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        lower = 0
        upper = len(height) -1
        max_area = 0

        while lower < upper:
            curr_area = min(height[lower], height[upper])*(upper-lower)
            max_area = curr_area if curr_area > max_area else max_area

            if height[lower] <= height[upper]:
                lower += 1
            else:
                upper -= 1


        return max_area
        


class SolTest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.test = [1,8,6,2,5,4,8,3,7]

    def test_one(self):
        self.assertEqual(self.sol.maxArea(self.test), 49)


if __name__ == "__main__":
    unittest.main()
