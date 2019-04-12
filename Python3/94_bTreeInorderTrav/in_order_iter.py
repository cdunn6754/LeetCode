import unittest

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
        stack = []
        ret = []

        if root == None:
            return []
        
        while len(stack) or not root == None:
            while(not root == None):
                stack.append(root)
                root = root.left

            root = stack.pop()
            ret.append(root.val)
            root = root.right

        return ret
        
        

class testit(unittest.TestCase):
    def setUp(self):
        self.r = TreeNode(1)
        self.r.right = TreeNode(2)
        self.r.right.left = TreeNode(3)

        self.sol = Solution()

    def test_1(self):
        self.assertEqual(self.sol.inorderTraversal(self.r), [1,3,2])

unittest.main()
