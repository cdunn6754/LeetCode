import unittest

class Solution:
    def possible_next_steps(self, word):
        if word in self.memo_next_steps:
            return self.memo_next_steps[word]
        
        res = set()
        to_remove = []
        for sw in self.word_set:
            if sw in self.memo_next_steps:
                continue
            count = 0
            for (wl, swl) in zip(word, sw):
                if not wl == swl:
                    count += 1
                if count > 1:
                    break
            if count == 1:
                res.add(sw)
                to_remove.append(sw)

        for w in to_remove:
            self.word_set.remove(w)
            
        self.memo_next_steps[word] = res
        return res
        
        
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        self.word_set = set(wordList)
        if not endWord in self.word_set:
            return 0

        self.memo_next_steps = {}
        nq = {beginWord}
        ladder_len = 1

        while len(nq) > 0:
            ladder_len += 1
            q, nq = nq, set()
            while len(q) > 0:
                w = q.pop()
                if not w in self.memo_next_steps:
                    next_words = self.possible_next_steps(w)
                    nq.update(next_words)
            if endWord in nq:
                return ladder_len
            
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
