import unittest

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        word_set = set(wordDict)

        rw = ""
        letters_left = len(s)
        
        for l in s:
            rw += l
            if rw in word_set:
                letters_left -= len(rw)
                rw = ""
        return letters_left == 0
            
            
        
class wbTest(unittest.TestCase):
    def test_wb(self):
        sol = Solution()

        self.assertTrue(sol.wordBreak("aaaaaaa", ["aaaa", "aaa"]))
        self.assertTrue(sol.wordBreak("leetcode", ["leet", "code"]))
        self.assertFalse(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

unittest.main()
