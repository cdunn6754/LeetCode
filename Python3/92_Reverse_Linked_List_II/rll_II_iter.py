import unittest 

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverse_x(self, head, x):

        curr = head
        p = n = None
        counter = 0
        #import pdb; pdb.set_trace()
        while curr and counter <= x:
            n = curr.next
            curr.next = p
            p = curr
            curr = n

            counter += 1

        # set the original head of this list to point at the
        # value that comes after (maybe None)
        head.next = curr
        
        return p
    
    def reverseBetween(self, head: ListNode, m: int, k: int) -> ListNode:

        if head == None or head.next == None:
            return head

        curr = head
        p = None

        counter = 1

        while counter < m:
            p = curr
            curr = curr.next
            counter += 1

        # now m == counter
        lower = p
        #import pdb; pdb.set_trace()
        rll_head = self.reverse_x(curr, k-m)

        if lower != None:
            lower.next = rll_head
            return head
        else:
            return rll_head
            
        



def get_val_list(head):
    val_list = []
    while head:
        val_list.append(head.val)
        head = head.next

    return val_list


class rllTest(unittest.TestCase):
    def setUp(self):
         self.s = Solution()
         head = ListNode(1)
         head.next = ListNode(2)
         head.next.next = ListNode(3)
         head.next.next.next = ListNode(4)
         head.next.next.next.next = ListNode(5)
         self.head = head

    def test_reverse_x_1(self):
        #import pdb; pdb.set_trace()
        c = self.s.reverse_x(self.head, 2)
        self.assertEqual(get_val_list(c), [3,2,1,4,5])        
        
    def test_reverse_x_2(self):
        
        r = self.head.next
        c = self.s.reverse_x(r, 2)
        self.assertEqual(get_val_list(c), [4,3,2,5])

    def test_reverseBetween(self):

        r = self.head
        nh = self.s.reverseBetween(r, 2, 4)
        self.assertEqual(get_val_list(nh), [1,4,3,2,5])

    def test_reverseBetween2(self):
        r = self.head
        nh = self.s.reverseBetween(r, 1, 4)
        self.assertEqual(get_val_list(nh), [4,3,2,1,5])

    def test_reverseBetween3(self):
        r = self.head
        nh = self.s.reverseBetween(r, 1, 5)
        self.assertEqual(get_val_list(nh), [5,4,3,2,1])

    def test_reverseBetween4(self):
        r = self.head
        nh = self.s.reverseBetween(r, 3, 5)
        self.assertEqual(get_val_list(nh), [1,2,5,4,3])

    def test_reverseBetween4(self):
        r = None
        nh = self.s.reverseBetween(r, 3, 5)
        self.assertEqual(nh, None)
        

unittest.main()
