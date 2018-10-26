class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = len(s)
        if len(s) < 2:
            return s

        mid = l//2
        return self.reverseString(s[mid:]) + self.reverseString(s[0:mid])



s = Solution()
test = "A man, a plan, a canal: Panama"

print(s.reverseString(test))



