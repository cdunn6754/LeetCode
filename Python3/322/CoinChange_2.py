class Solution:

    def __init__(self):
        self.memo = {}
        self.memo[0] = 0
    
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        #memo = [None]*(amount+1)
        #memo[0] = 0
        num = self.F(coins, amount, memo)
        return num


    def F(self, coins, amount, memo):
        if memo.get(amount) != None: #memo[amount] != None:
            return memo[amount]

        best = amount+1
        for coin in coins:
            if amount - coin >= 0:
                temp = self.F(coins, amount-coin, memo)
                if temp != -1 and temp < best:
                    best = temp
                    
        if best != amount+1:
            memo[amount] = best + 1
            return memo[amount]
        memo[amount] = -1
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
