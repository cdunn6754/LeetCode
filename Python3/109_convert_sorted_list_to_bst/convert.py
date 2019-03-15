# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return None

        if head.next == None:
            return TreeNode(head.val)

        # find the middle
        end_n = head.next.next
        mid_n = head
        while end_n != None and end_n.next != None:
            end_n = end_n.next.next
            mid_n = mid_n.next

        temp = mid_n.next
        mid_n.next = None
        mid_n = temp
        
        end_n = mid_n.next
        
        bst_node = TreeNode(mid_n.val)
        bst_node.left = self.sortedListToBST(head)
        bst_node.right = self.sortedListToBST(end_n)

        return bst_node
        
