class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype
        """

        sum = max_sum = nums[0]
        
        for n in nums[1:]:

            sum = max(sum + n, n)
            max_sum = max(sum, max_sum)

        return max_sum


test1 = [-2,1,-3,4,-1,2,1,-5,4]
s=Solution()
print(s.maxSubArray(test1))
