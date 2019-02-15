class Solution:
    def reverseOnlyLetters(self, S: 'str') -> 'str':

        if len(S) <= 1:
            return S

        new_list = list(S)
        lower = 0
        upper = len(S) -1
        
        if S.isalpha():    
            while upper > lower:
                new_list[lower], new_list[upper] = S[upper], S[lower]
                lower += 1
                upper -= 1
            return ''.join(new_list)

        while upper > lower:
            if not S[lower].isalpha():
                lower += 1
                continue
            if not S[upper].isalpha():
                upper -= 1
                continue
            new_list[lower], new_list[upper] = S[upper], S[lower]
            lower += 1
            upper -= 1            
        return ''.join(new_list)
        
        



sol = Solution()

test=["h-iyab_uddy", "", "a", "-", "a-", "_b", "!-", "ab"]


for s in test:
    print(sol.reverseOnlyLetters(s))
            

        
