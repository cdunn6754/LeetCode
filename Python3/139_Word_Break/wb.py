import unittest

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        known = {0,}

        for i in range(len(s) + 1):
            if i in known:
                for w in wordDict:
                    #import pdb; pdb.set_trace()
                    next_idx = i + len(w)
                    if s[i:next_idx] == w:
                        if next_idx == len(s):
                            return True
                        known.add(next_idx)
        return False
        
class wbTest(unittest.TestCase):
    def test_wb(self):
        sol = Solution()

        self.assertTrue(sol.wordBreak("cars", ["car", "ca", "rs"]))
        self.assertTrue(sol.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
        self.assertTrue(sol.wordBreak("leetcode", ["leet", "code"]))
        self.assertFalse(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

unittest.main()
