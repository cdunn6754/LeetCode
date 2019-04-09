import unittest
import collections

class Solution:        
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        combo_dict = collections.defaultdict(list)

        L = len(beginWord)
        
        for word in wordList:
            for i in range(L):
                k = word[:i] + "*" + word[i+1:]
                combo_dict[k].append(word)

        visited = {beginWord,}
        q = [(beginWord, 1)]

        while len(q) > 0:
            tup = q.pop(0)          
            if tup[0] == endWord:
                return tup[1]
            
            for i in range(L):
                k = tup[0][:i] + "*" + tup[0][i+1:]
                for w in combo_dict[k]:
                    if not w in visited:
                        q.append((w, tup[1]+1))
                        visited.add(w)
        return 0

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

        self.assertFalse(sol.ladderLength(bw, ew, wl))
        
unittest.main()
