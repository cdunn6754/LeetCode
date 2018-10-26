# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        d = False
        (_, d) = self.recursiveRemover(head,n,d)
        if not d:
            head = head.next

        return head

    def recursiveRemover(self, head,n,d):

        if not head.next:
            return (1, d)
        (fromEnd,d) = self.recursiveRemover(head.next, n, d)
        if fromEnd == n:
            head.next = head.next.next
            d = True
            
        return (1 + fromEnd, d)
        

        

        
            
s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

n = 3
r = s.removeNthFromEnd(head, n)
while r:
    print(r.val)
    r = r.next
