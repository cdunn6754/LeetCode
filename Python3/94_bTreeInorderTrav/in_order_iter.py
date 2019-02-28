# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        stack = [root]
        ret = []

        if root == None:
            return []
        while len(stack):
            curr = stack[-1]
            while curr.left and not curr.left.val in ret:
                curr = curr.left
                stack.append(curr)
            ret.append(stack.pop().val)
            if curr.right:
                stack.append(curr.right)

        return ret
        
        
