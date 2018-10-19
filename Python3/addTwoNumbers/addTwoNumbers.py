# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        return_list_head = ListNode(-1)
        temp_node = return_list_head
        first_time = True

        remainder = 0

        # still numbers left in one list
        numbers_left_1 = True
        numbers_left_2 = True

        while (numbers_left_1 or numbers_left_2 or remainder == 1):
            
            if (l1):
                num_1 = l1.val
            else:
                num_1 = 0

            if (l2):
                num_2 = l2.val
            else:
                num_2 = 0
                
            new_sum = remainder + num_1 + num_2

            remainder = 0
            
            if (new_sum > 9):
                new_sum = new_sum - 10
                remainder = 1


            temp_node.val = new_sum
            

            if (l1 and l1.next):
                l1 = l1.next
            else:
                l1 = None
                numbers_left_1 = False

            if (l2 and l2.next):
                l2 = l2.next
            else:
                l2 = None
                numbers_left_2 = False

            if (numbers_left_2 or numbers_left_1 or remainder):
                new_temp_node = ListNode(-1)
                temp_node.next = new_temp_node

                temp_node = temp_node.next
                
            
        return return_list_head
        
### END SOLUTION
### TESTING 
Solution1 = Solution()

# make some test lists
l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)

l11.next = l12
l12.next = l13

l21 = ListNode(5)
l22 = ListNode(6)
l23 = ListNode(4)

l21.next = l22
l22.next = l23

# call the function
print(Solution1.addTwoNumbers(l11,l21).next.next.val)
