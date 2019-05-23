# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def in_order(self, node, l):
        if node.left != None:
            self.in_order(node.left, l)
        l.append(node.val)
        if node.right != None:
            self.in_order(node.right, l)
        return l
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True

        l_root = root.left
        r_root = root.right

        if l_root == None and r_root == None:
            return True

        if l_root != None and r_root == None:
            return False

        if l_root == None and r_root != None:
            return False

        if l_root.val != r_root.val:
            return False

        l = []
        r = []

        l_list = self.in_order(l_root, l)
        r_list = self.in_order(r_root, r)

        for (r,l) in zip(l_list, reversed(r_list)):
            if r != l:
                return False
        return True

        

        
