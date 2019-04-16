import unittest
import collections

class Solution:
    def totalFruit(self, tree) -> int:

        if len(tree) < 3:
            return len(tree)
        types_counter = collections.defaultdict(int)
        lo_tree = 0
        types_counter[tree[lo_tree]] += 1


        max_num_fruit = 0

        for hi_tree in range(1, len(tree)):
            types_counter[tree[hi_tree]] += 1

            while len(types_counter) > 2:
                lo_val = tree[lo_tree]
                types_counter[lo_val] -= 1
                if types_counter[lo_val] == 0:
                    del types_counter[lo_val]
                lo_tree += 1
                
            curr_num_fruit = hi_tree - lo_tree + 1

            max_num_fruit = max(curr_num_fruit, max_num_fruit)

        return max_num_fruit
        
class TestFIB(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        
    def test_1(self):
        self.assertEqual(self.sol.totalFruit([1,2,1]), 3)

    def test_2(self):
        self.assertEqual(self.sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]), 5)
        
unittest.main()
