class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        return self.F(coins, amount)
    
    def __init__(self):
        self.F_memo = {}
        self.F_memo[0] = 0


    def F(self, coins, amount):
        try:
            return self.F_memo[amount]
        except KeyError:
            pass
        if all(amount < c for c in coins):
            self.F_memo[amount] = -1
            return -1

        try: 
            self.F_memo[amount] = min(
                [self.F(coins, amount - c) for
                 c in coins
                 if self.F(coins, amount - c) != -1]
            ) + 1

            return self.F_memo[amount]
        except ValueError:
            return -1


sol = Solution()

F_tests = [
    ([1,2,5], 100),
    ([3,4], 0),
    ([3,4], 6),
]

for test in F_tests:
    print(sol.F(*test))
