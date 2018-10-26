class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = nums[0]
        c_sum = nums[0]

        for num in nums[1:]:

            if c_sum + num > c_sum:
                c_sum += num
            else:
                c_sum = num

            if c_sum > max_sum:
                max_sum = c_sum

        return max_sum
