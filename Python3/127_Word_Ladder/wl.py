import unittest

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        pass


class wlTest(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        bw = "hit"
        ew = "cog"
        wl = ["hot","dot","dog","lot","log","cog"]

        self.assertEqual(sol.ladderLength(bw, ew, wl), 5)

    def test_2(self):
        sol = Solution()
        bw = "hit"
        ew = "cog"
        wl = ["hot","dot","dog","lot","log"]

        self.assertEqual(sol.ladderLength(bw, ew, wl), 5)        
unittest.main()
