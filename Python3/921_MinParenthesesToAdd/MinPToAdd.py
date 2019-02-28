class Solution:
    def minAddToMakeValid(self, S: 'str') -> 'int':

        if len(S) == 0:
            return 0
        
        stack = [S[0]]

        for c in S[1:]:
            if len(stack) != 0 and (stack[-1] == "(" and c == ")"):
                stack.pop()
            else:
                stack.append(c)

        return len(stack)

sol = Solution()

tests = [
    "())",
    "()",
    "(()",
    ")(",
    "",
]

for test in tests:
    print(sol.minAddToMakeValid(test))
            
