# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        
        cc = 1
        nc = 0
        depth = 0
        q = [root]

        while len(q) > 0:
            cc -= 1

            n = q.pop(0)
            if n.left:
                q.append(n.left)
                nc += 1
            if n.right:
                q.append(n.right)
                nc += 1

            if cc == 0:
                cc = nc
                nc = 0
                depth += 1

        return depth
