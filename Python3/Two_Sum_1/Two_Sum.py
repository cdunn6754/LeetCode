class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numidxs = {}

        for idx, num in enumerate(nums):
            if (target - num) in numidxs:
                return [numidxs[(target - num)], idx]
            numidxs[num] = idx

        

s = Solution()

tester = [2,7,11,15]

print(s.twoSum(tester,9))
