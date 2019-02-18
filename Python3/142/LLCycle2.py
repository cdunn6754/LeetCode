# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        l1 = l2 = head

        while True:
            try: 
                l1 = l1.next
                l2 = l2.next.next

                if l1 == l2:
                    break
                
            except AttributeError:
                return None            

        l1 = head

        while l1 != l2:
            l1 = l1.next
            l2 = l2.next

        return l1


sol = Solution()
            
            
