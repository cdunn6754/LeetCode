# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def r_preorder(root):
            if root == None:
                return None
            
            res.append(root.val)
            r_preorder(root.left)
            r_preorder(root.right)

        r_preorder(root)
        return res
        

        
