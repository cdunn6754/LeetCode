# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = deque([root])
        res = []

        if not root:
            return []

        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)            
            if curr.left:
                stack.append(curr.left)


        return res

        

        
