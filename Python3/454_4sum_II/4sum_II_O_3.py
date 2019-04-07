import unittest

class Solution:
    def fourSumCount(self, A, B, C, D) -> int:
        d_dict = {}
        count = 0
        
        for k in D:
            if d_dict.get(k) == None:
                d_dict[k] = 1
            else:
                d_dict[k] += 1
                
        for i in A:
            for j in B:
                for k in C:
                    needed = -(i + j + k)
                    if not d_dict.get(needed) == None:
                        count += d_dict[needed]
            
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
