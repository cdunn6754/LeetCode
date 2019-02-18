class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        ptr1 = 0

        while ptr1 < len(nums) and nums[ptr1] != 0:
            ptr1 += 1

        ptr2 = ptr1 + 1
        
        while ptr2 < len(nums) and nums[ptr2] == 0:
            ptr2 += 1
            
        while ptr2 < len(nums):
            if nums[ptr1] == 0 and nums[ptr2] != 0:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1
                ptr2 += 1
            elif nums[ptr1] == 0:
                ptr2 += 1
            elif nums[ptr2] != 0:
                ptr1 += 1
            else:
                ptr1 += 1
                ptr2 += 1                

sol = Solution()

tests = [
    [1,2,3],
    [1,2,3,0,0],    
    [0,1,0,3,12],
    [],
    [0],
    [1],
]


for test in tests:
    sol.moveZeroes(test)
    print(test)
            
