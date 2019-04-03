# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check_tree(self, root, lo=float("-inf"), hi=float("inf")):
        if root == None: return True
        
        if root.val > lo and root.val < hi:
            return(
                self.check_tree(root.left, lo, root.val)
                and
                self.check_tree(root.right, root.val, hi)
            )
        else:
            return False
        
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check_tree(root)

        
