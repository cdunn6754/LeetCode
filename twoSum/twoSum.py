class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for first_index, first_number in enumerate(nums):
            for second_index, second_number in enumerate(
                    nums[first_index + 1:]):
                if (first_number + second_number) == target:
                    second_return_index = first_index + second_index + 1
                    print(first_index, second_return_index)
                    return [first_index, second_return_index]

        


Solution1 = Solution()
print(Solution1.twoSum([3,2,4], 6))
