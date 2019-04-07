import unittest

class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        sum_dict = {}
        count = 0
        
        for c in C:
            for d in D:
                if sum_dict.get(c + d) == None:
                    sum_dict[c + d] = 1
                else:
                    sum_dict[c + d] += 1

        for a in A:
            for b in B:
                needed = -(a + b)
                if not sum_dict.get(needed) == None:                                      
                    count += sum_dict[needed]
        return count

class fsTest(unittest.TestCase):
    def test_lc(self):
        self.sol = Solution()
        
        a = [1,2]
        b = [-2,-1]
        c = [-1,2]
        d = [0,2]

        self.assertEqual(self.sol.fourSumCount(a,b,c,d), 2)

unittest.main()
