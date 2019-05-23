# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isPalindrome(self, arr):
        low = 0
        high = len(arr) -1

        while low < high:
            if not arr[low] == arr[high]:
                return False
            low += 1
            high -= 1
        return True
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right == None:
            return False
        if not root.left.val == root.right.val:
            return False
        
        nq = [root.left, root.right]
        q = []

        while not nq == []:
            q = nq
            nq = []
            vals = []

            # vals = [n.val for n in q]
            # if not self.isPalindrome(vals):
            #     return False

            while not q == []:
                node = q.pop(0)
                if node.left == None:
                    vals.append(None)
                else:
                    nq.append(node.left)
                    vals.append(node.left.val)
                    
                if node.right == None:
                    vals.append(None)
                else:
                    nq.append(node.right)
                    vals.append(node.right.val)

            print(vals)
            if not self.isPalindrome(vals):
                return False
        
        return True
