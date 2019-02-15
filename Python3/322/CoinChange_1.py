class Solution:

    def __init__(self):
        # which combinations of coins don't work 
        self.bad_stacks = []

    def clear_stack(self):
        self.bad_stacks = []
        
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        """
        Start with the highest possible amount and try to make it work.
        Record when those don't work
        """
        if amount == 0:
            return 0
        if (all(amount < value for value in coins)):
            return -1
        if amount in coins:
            return 1

        
        return self.check(coins, [], amount)
        
    def check(self, coins, stack, amount):
        try: 
            base_coin = max([c for c in coins if
                             (not tuple(stack+[c]) in self.bad_stacks) and
                             ((sum(stack) + c) <= amount)
            ])
        except ValueError:
            # there is no coin that will work
            self.bad_stacks.append(tuple(stack))
            return -1
        

        # otherwise add it to the pile
        stack.append(base_coin)
        # maybe this is the one that did it
        if sum(stack) == amount:
            return len(stack)
        # if not then keep trying
        res = self.check(coins, stack, amount)
        
        #import pdb; pdb.set_trace()        

        # if res is good then we found it
        if res != -1:
            return res

        # if it didn't work out then call this funciton again
        # the most recent attempted addition will not be tried
        # again
        stack.pop()
        return self.check(coins, stack, amount)

sol = Solution()

tests = [
    ([1], 0),
    ([], 5),
    ([1,2,5], 11),
    ([3,7], 9),    
    ([1,3,7], 9),
    ([1,2,3], 2),
    ([4,5,6], 3),
    ([2], 3),
]

for test in tests:
    print(sol.coinChange(*test))
    sol.clear_stack()
