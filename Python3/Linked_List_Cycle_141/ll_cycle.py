# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head or head.next == None:
            return False

        faster = head

        while faster and faster.next:
            head = head.next
            faster = faster.next.next

            if head == faster:
                return True

        return False
        
