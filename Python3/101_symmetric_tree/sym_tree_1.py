# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

    def isMirror(self, n1, n2):
        if n1 == None and n2 == None:
            return True
        if n1 == None or n2 == None:
            return False
        
        return (
            (n1.val == n2.val) and
            self.isMirror(n1.left, n2.right) and
            self.isMirror(n1.right, n2.left)
        )
