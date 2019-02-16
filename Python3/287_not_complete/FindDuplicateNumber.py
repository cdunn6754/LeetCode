class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        ptr1 = ptr2 = 0

        while True:
            ptr1 = nums[ptr1]
            ptr2 = nums[nums[ptr2]]

            if nums[ptr1] == nums[ptr2]:
                cycle_val

        ptr1 = 0
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]            
            
