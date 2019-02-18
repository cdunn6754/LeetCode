class Solution:
    def findDuplicate(self, nums: 'List[int]') -> 'int':
        ptr1 = ptr2 = 0

        while True:
            ptr1 = nums[ptr1]
            ptr2 = nums[nums[ptr2]]

            if nums[ptr1] == nums[ptr2]:
                break
        ptr1 = 0
        while nums[ptr1] != nums[ptr2]:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return nums[ptr1]


sol = Solution()
tests = [
    [1,3,4,2,2],
    [2,5,9,6,9,3,8,9,7,1]    
]

for test in tests:
    print(sol.findDuplicate(test))
