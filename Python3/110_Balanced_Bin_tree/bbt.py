# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, depth):
        
        if root == None:
            return (True, depth)

        depth += 1
        l_bal, l_depth = self.dfs(root.left, depth)
        r_bal, r_depth = self.dfs(root.right, depth)

        if l_bal and r_bal:
            bal = abs(l_depth - r_depth) <= 1
        else:
            bal = False

        return (bal, max(l_depth, r_depth))
            
    def isBalanced(self, root: TreeNode) -> bool:

        if root == None:
            return True

        bal, _ = self.dfs(root, 0)

        return bal

        
        
                
        
        
                
        

            




                
