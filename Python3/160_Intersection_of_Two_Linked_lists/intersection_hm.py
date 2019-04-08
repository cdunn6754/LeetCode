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

        node_ids = set()

        while not headA == None and not headB == None:
            
            if id(headA) in node_ids:
                return headA
            node_ids.add(id(headA))
            
            if id(headB) in node_ids:
                return headB
            node_ids.add(id(headB))
            
            headA = headA.next
            headB = headB.next

        while not headA == None:
            if id(headA) in node_ids:
                return headA
            headA = headA.next

        while not headB == None:
            if id(headB) in node_ids:
                return headB
            headB = headB.next            

        return None

        
