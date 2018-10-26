class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s.strip()
        words = []

        i = 0
        while i < len(s):

            if not s[i] == " ":
                word_start = i
                
                while i < len(s) and not s[i] == " ":
                    i += 1

                words.append(s[word_start:i])
            i += 1

        words.reverse()
        return " ".join(words)


s = Solution()
test = "the sky is blue"
print(s.reverseWords(test))
                
            
