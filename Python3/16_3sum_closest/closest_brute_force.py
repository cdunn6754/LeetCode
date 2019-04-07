import unittest


class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        # nums.sort()

        # lower = set()
        # best_diff = float('inf')
        # best_result = None

        # remaining = {}
        # for n in nums:
        #     if remaining.get(n) == None:
        #         remaining[n] = 1
        #     else:
        #         reminaing[n] += 1

        # for n in num:
        #     remaining[n] -= 1

        #     for ln in lower:
        #         diff = target - (n + ln

        #     lower.add(n)
        

        best_diff = float('inf')
        closest = None
        
        for i_idx, i in enumerate(nums):
            for j_idx, j in enumerate(nums[i_idx + 1:]):
                for k in nums[i_idx + j_idx + 2:]:
                    diff = abs(target - (i + j + k))
                    if diff < best_diff:
                        best_diff = diff
                        closest = (i + j + k)
        return closest

class TestClosest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testClosest(self):
        arr = [-1, 2, 1, -4]
        self.assertEqual(self.sol.threeSumClosest(arr, 1), 2)

        arr = [1,1,1,0]
        self.assertEqual(self.sol.threeSumClosest(arr, 1), -100)


if __name__ == "__main__":
    unittest.main()
