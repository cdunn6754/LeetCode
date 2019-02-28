# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self, root, ret):
        if root.left:
            self.inorder(root.left, ret)
        ret.append(root.val)
        if root.right:
            self.inorder(root.right, ret)
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        ret = []
        if root:
            self.inorder(root, ret)
        return ret
        
        
