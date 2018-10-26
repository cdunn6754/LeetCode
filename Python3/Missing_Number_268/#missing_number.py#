class Solution:
    """
    O(n) time complexity (from the sum) and constant space complexity.
    """
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l_e = len(nums)
        expected_sum = (l_e * (l_e+1))/2

        return int(expected_sum - sum(nums))



s = Solution()
test1 = [3,2,1]

print(s.missingNumber(test1))
