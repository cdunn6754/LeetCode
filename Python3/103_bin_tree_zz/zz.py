# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if root == None:
            return []

        q = []
        nq = [root]

        res = []

        zag = True

        while len(nq) > 0:            
            res.append([n.val for n in nq])
            q, nq = nq, []
            
            while len(q) > 0:
                n = q.pop()
                if zag:
                    if n.right != None:
                        nq.append(n.right)                    
                    if n.left != None:
                        nq.append(n.left)
                else:
                    if n.left != None:
                        nq.append(n.left)
                    if n.right != None:
                        nq.append(n.right)

            zag = not zag

        return res
            
            
            
