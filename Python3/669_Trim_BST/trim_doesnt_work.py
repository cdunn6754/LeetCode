# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def find_left(self, root, val):
        if root == None or root.val <= val:
            return root
        return self.find_left(root.left, val)

    def find_right(self, root, val):
        if root == None or root.val >= val:
            return root
        return self.find_right(root.right,val)

    def trim_left(self, root, L):
        if root == None:
            return None
        if root.val < L:
            return self.find_right(root, L)
        
        root.left = self.trim_left(root.left, L)
        return root
    
    def trim_right(self, root, R):
        if root == None:
            return None
        if root.val > R:
            return self.find_left(root, R)

        root.right = self.trim_right(root.right, R)
        return root
        
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        if root.val < L:
            root = self.find_right(root, L)
        elif root.val > R:
            root = self.find_left(root, R)

        if root == None:
            return None


        root = self.trim_left(root, L)
        root = self.trim_right(root, R)
        return root
        
        
        

        
            
