import unittest
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ll_to_num(self, ll: ListNode) -> int:
        """Given a digit ll in reverse order return the number"""
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
        return head
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_num = self.ll_to_num(l1) + self.ll_to_num(l2)
        return self.num_to_ll(sum_num)
        


class SolTest(unittest.TestCase):

    def setUp(self):
        self.ll1 = ListNode(2)
        self.ll1.next = ListNode(4)
        self.ll1.next.next = ListNode(3)

        self.ll2 = ListNode(5)
        self.ll2.next = ListNode(6)
        self.ll2.next.next = ListNode(4)

        self.res = ListNode(7)
        self.res.next = ListNode(0)
        self.res.next.next = ListNode(8)
        
        self.sol = Solution()

    def test_ll_to_num(self):
        self.assertEqual(self.sol.ll_to_num(self.ll1), 342)
        self.assertEqual(self.sol.ll_to_num(self.ll2), 465)

    def test_num_to_ll(self):
        self.assertEqual(self.sol.num_to_ll(342).val, self.ll1.val)
        self.assertEqual(self.sol.num_to_ll(465).val, self.ll2.val)

        self.assertEqual(
            self.sol.ll_to_num(self.sol.num_to_ll(342)),
            342
        )

    def test_integration(self):
        self.assertEqual(
            self.sol.ll_to_num(self.sol.addTwoNumbers(self.ll1, self.ll2)),
            807
        )

        
        
if __name__ == '__main__':
    unittest.main()
