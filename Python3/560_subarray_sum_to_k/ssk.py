import unittest
import collections

class Solution:
    def subarraySum(self, nums, k: int) -> int:
        count = 0

        cs_dict = collections.defaultdict(int)
        
        cs = 0
        
        for num in nums:
            cs += num
            count += cs_dict[cs - k]
            if cs == k: count += 1
            
            cs_dict[cs] += 1
            
            

        return count
        

class testSSK(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.subarraySum([1,1,1], 2), 2)

unittest.main()
