# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        stackA = []
        stackB = []
        
        while headA != None:
            stackA.append(headA)
            headA = headA.next

        while headB != None:
            stackB.append(headB)
            headB = headB.next
            
        if len(stackA) == 0 or len(stackB) == 0:
            return None
        
        prev = None
        
        while headA == headB:
            prev = headA
            if len(stackA) == 0 or len(stackB) == 0:
                break
            headA = stackA.pop()
            headB = stackB.pop()

        return prev
