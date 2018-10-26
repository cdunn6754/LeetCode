class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0:
            return True
        if len(s)== 1:
            return False

        stack = []
        closing = [")", "}", "]"]
        match = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        if s[0] in closing:
            return False
        
        for l in s:
            if l in closing:                
                if len(stack) == 0 or not match.get(stack.pop(),None) == l:
                    return False
            else:
                stack.append(l)
            
        if len(stack) == 0:
            return True

        return False

s = Solution()
test = "{[)}"

print(s.isValid(test))
