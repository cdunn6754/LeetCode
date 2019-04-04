import unittest

class Solution:

    @staticmethod
    def has_dupes(s):
        return not (len(set(s)) == len(s))
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo = 0
        hi = 2
        l = len(s)
        
        if l < 2:
            return l

        max_len = 1
        while hi <= l:
            if self.has_dupes(s[lo:hi]):
                lo += 1
                hi += 1
            else:
                if hi - lo  > max_len:
                    max_len = hi - lo
                hi += 1

        return max_len


class TestIt(unittest.TestCase):

    def test1(self):
        sol = Solution()
        self.assertEqual(3, sol.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, sol.lengthOfLongestSubstring("bbbbbb"))
        self.assertEqual(3, sol.lengthOfLongestSubstring("pwwkew"))

unittest.main()
