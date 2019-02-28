class Solution:
    def climbStairs(self, n: int) -> int:

        self.memo = [None]*(n+1)
        self.memo[0:4] = [0, 1, 2, 3]

        return self.climbStairsR(n)

    def climbStairsR(self, n):
        if self.memo[n] != None:
            return self.memo[n]
        else: 
            res = self.climbStairsR(n-1) + self.climbStairsR(n-2)
            self.memo[n] = res
            return res


sol = Solution()

print(sol.climbStairs(4))
    
        

    
