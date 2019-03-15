# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """recursively convert a sorted array into a bst"""

        if len(nums) == 0:
            return None
        
        mid_idx = len(nums)//2

        node = TreeNode(nums[mid_idx])
        node.left = self.r_convert(nums[0:mid_idx])
        try:
            node.right = self.r_convert(nums[mid_idx + 1:])
        except IndexError:
            node.right = None

        return node
