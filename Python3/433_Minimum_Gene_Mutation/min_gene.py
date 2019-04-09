import unittest
import collections

class Solution:
    def minMutation(self, start: str, end: str, bank) -> int:

        if not end in bank or not bank:
            return -1

        conn = collections.defaultdict(list)
        
        L = len(start)
        for g in bank:
            for i in range(L):
                k = g[:i] + "*" + g[i+1:]
                conn[k].append(g)
        q = [(start, 0)]
        visited = {start}

        while len(q) > 0:
            g, num = q.pop(0)
            if g == end:
                return num
            for i in range(L):
                k = g[:i] + "*" + g[i+1:]
                for ng in conn[k]:
                    if not ng in visited:
                        visited.add(ng)
                        q.append((ng, num+1))

        return -1
        

class mgmTest(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()
        
    def test_1(self):
        s = "AACCGGTT"
        e = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

        self.assertEqual(self.sol.minMutation(s,e,bank), 2)

    def test_2(self):
        s = "AAAAACCC"
        e = "AACCCCCC"
        bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

        self.assertEqual(self.sol.minMutation(s,e,bank), 3)        

    
unittest.main()
