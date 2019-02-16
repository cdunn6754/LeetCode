class Solution:

    def __init__(self):
        self.memo = {}
        self.memo[0] = 0
    
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        num = self.F(coins, amount)
        return num


    def F(self, coins, amount):
        if self.memo.get(amount) != None:
            return self.memo[amount]

        try:
            self.memo[amount] = min(
                [self.F(coins, amount-c) for c in coins if amount - c >= 0]
            ) + 1

        except ValueError:
            return -1


sol = Solution()

F_tests = [
    ([1,2,5], 100),
    ([3,4], 5),
    ([3,4], 10),
    ([3,4], 0),
    ([3,4], 1),
    ([186, 419, 83, 408], 6249)
]

for test in F_tests:
    print(sol.coinChange(*test))
