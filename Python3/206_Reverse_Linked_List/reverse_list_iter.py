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
        if not head:
            return head
        
        if not head.next:
            return head
        
        if not head.next.next:
            n_node = head.next
            head.next = None
            n_node.next = head
            return n_node

        temp = head.next
        head.next = None
        n_node = temp.next
        temp.next = head
        head = temp

        while n_node.next:
            temp = n_node.next
            n_node.next = head
            head = n_node
            n_node = temp

        n_node.next = head
        return n_node

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

print(r.val, r.next.val,
      r.next.next.val, r.next.next.next.val, r.next.next.next.next.val)

