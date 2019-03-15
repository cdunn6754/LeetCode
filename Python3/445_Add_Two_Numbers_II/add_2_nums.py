import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse_list(self, ll: ListNode) -> ListNode:
        curr = ll
        p = n = None

        while curr != None:
            n = curr.next
            curr.next = p
            p = curr
            curr = n
        return p
        
    def ll_to_num(self, ll: ListNode) -> int:
        """Given a digit ll in reverse order return the number"""
        ll = self.reverse_list(ll)
        power = 1
        number = 0
        while ll != None:
            number += power * ll.val
            power *= 10
            ll = ll.next
        return number
    
    def num_to_ll(self, num: int) -> ListNode:
        """given an int return the reverse ordered ll"""

        head = ListNode(num % 10)
        num = num // 10

        curr_n = head
        
        while num > 0:
            curr_n.next = ListNode(num%10)
            num = num//10
            curr_n = curr_n.next
        return self.reverse_list(head)
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_num = self.ll_to_num(l1) + self.ll_to_num(l2)
        return self.num_to_ll(sum_num)
        


class SolTest(unittest.TestCase):

    def setUp(self):
        self.ll1 = ListNode(7)
        self.ll1.next = ListNode(2)
        self.ll1.next.next = ListNode(4)
        self.ll1.next.next.next = ListNode(3)

        self.ll2 = ListNode(5)
        self.ll2.next = ListNode(6)
        self.ll2.next.next = ListNode(4)

        self.res = ListNode(7)
        self.res.next = ListNode(8)
        self.res.next.next = ListNode(0)
        self.res.next.next.next = ListNode(7)
        
        self.sol = Solution()

    def test_ll_to_num(self):
        self.assertEqual(self.sol.ll_to_num(self.ll1), 7243)
        self.assertEqual(self.sol.ll_to_num(self.ll2), 564)

    def test_num_to_ll(self):
        self.assertEqual(self.sol.num_to_ll(7243).val, self.ll1.val)
        self.assertEqual(self.sol.num_to_ll(564).val, self.ll2.val)

        self.assertEqual(
            self.sol.ll_to_num(self.sol.num_to_ll(745)),
            745
        )

    def test_integration(self):
        self.assertEqual(
            self.sol.ll_to_num(self.sol.addTwoNumbers(self.ll1, self.ll2)),
            7807
        )

        
        
if __name__ == '__main__':
    unittest.main()
