# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = n_node = None
        curr = head

        while curr:
            n_node = curr.next
            curr.next = prev
            prev = curr
            curr = n_node

        return prev
class ListNode:
    def __init__(self,val):
        self.next = None
        self.val = val
        
s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

r = s.reverseList(head)

while r:
    print(r.val)
    r = r.next

