# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        nq = [root]
        avg = []

        while len(nq) > 0:
            q, nq = nq, []

            vals = [n.val for n in q]
            avg.append(sum(vals)/len(vals))

            while len(q) > 0:
                n = q.pop(0)

                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)

        return avg
