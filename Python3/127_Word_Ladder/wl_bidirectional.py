import unittest
import collections

class Solution:        
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:

        if (not endWord in wordList) or not wordList:
            return 0
        
        combo_dict = collections.defaultdict(list)

        L = len(beginWord)
        
        for word in wordList:
            for i in range(L):
                k = word[:i] + "*" + word[i+1:]
                combo_dict[k].append(word)

        visited_1 = {beginWord: 1}
        visited_2 = {endWord: 1}
        q1 = [(beginWord, 1)]
        q2 = [(endWord, 1)]

        while len(q1) > 0 and len(q2) > 0:
            tup = q1.pop(0)
            if tup[0] == endWord:
                return tup[1]
            if tup[0] in visited_2:
                return tup[1] + visited_2[tup[0]] - 1
            
            for i in range(L):
                k = tup[0][:i] + "*" + tup[0][i+1:]
                for w in combo_dict[k]:
                    if not w in visited_1:
                        q1.append((w, tup[1]+1))
                        visited_1[w] = tup[1] + 1

            tup = q2.pop(0)
            if tup[0] == beginWord:
                return tup[1]
            if tup[0] in visited_1 :
                return tup[1] + visited_1[tup[0]] - 1
            
            for i in range(L):
                k = tup[0][:i] + "*" + tup[0][i+1:]
                for w in combo_dict[k]:
                    if not w in visited_2:
                        q2.append((w, tup[1]+1))
                        visited_2[w] = tup[1] + 1
       
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
