import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    def rReverse(self, head, back):
        
        if head.next == None:
            head.next = back
            return head
        n = head.next
        return self.rReverse(n, head)
        
        
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        
        return self.rReverse(head, None)
        

class RLLTest(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_reverse(self):
        n = ListNode(1)
        n.next = ListNode(2)
        n.next.next = ListNode(3)

        rl = self.sol.reverseList(n)
        
        self.assertEqual(rl.val, 3)
        self.assertEqual(rl.next.val, 2)
        self.assertEqual(rl.next.next.val, 3)

unittest.main()
