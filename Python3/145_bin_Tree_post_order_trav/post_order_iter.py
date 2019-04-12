import unittest
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __str__(self):
        return "Tree node: val={}".format(self.val)

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        stack = deque([])
        ret = []

        curr = root
        
        while len(stack) > 0 or not curr == None:

            while curr:
                stack.append(curr)
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
            
            curr = stack.pop()
           
                
            ret.append(curr.val)
            curr = None
            
        return ret
        
        

class testit(unittest.TestCase):
    def setUp(self):
        self.r = TreeNode(1)
        self.r.right = TreeNode(2)
        self.r.right.left = TreeNode(3)

        self.sol = Solution()

    def test_1(self):
        self.assertEqual(self.sol.inorderTraversal(self.r), [3,2,1])

unittest.main()
