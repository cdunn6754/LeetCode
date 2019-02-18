class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if nums == []:
            return 0

        if len(nums) == 1:
            return 0 if nums[0] == val else 1

        swap_idx = -1
        while swap_idx > -len(nums) and nums[swap_idx] == val:
            swap_idx -= 1
            
        if swap_idx == -len(nums):
            return 0 if nums[swap_idx] == val else 1

        for idx,num in enumerate(nums):
            if num == val:
                nums[idx], nums[swap_idx] = nums[swap_idx], nums[idx]
                swap_idx -= 1
                while nums[swap_idx] == val:
                    swap_idx -= 1
            if idx == swap_idx + len(nums):
                return idx + 1





sol = Solution()

print(sol.removeElement([4,5], 5))
