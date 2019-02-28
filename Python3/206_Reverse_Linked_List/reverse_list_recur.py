# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse_recursive(self, n1, n2):
        
        if n2 == None:
            return n1
        
        temp = n2.next
        n2.next = n1
        n1 = n2
        n2 = temp

        return self.reverse_recursive(n1, n2)

        
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next == None:
            return head
    
        n2 = head.next
        head.next = None
        return self.reverse_recursive(head, n2)



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


