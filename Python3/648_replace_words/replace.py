from unittest import TestCase, main
class Solution:
    def replaceWords(self, dict, sentence) -> str:
        roots = set(dict)

        ls = sentence.split(" ")
        for word_idx, word in enumerate(ls):
            root = ""
            for letter in word:
                root += letter
                if root in roots:
                    ls[word_idx] = root
                    break

        return(" ".join(ls))
                    
            

class rrTest(TestCase):
    def test_lc(self):
        sol = Solution()
        d = ["cat", "bat", "rat"]
        s = "the cattle was rattled by the battery"
        o = "the cat was rat by the bat"

        self.assertEqual(sol.replaceWords(d, s), o)

main()
