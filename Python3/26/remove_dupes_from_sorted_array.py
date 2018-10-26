class Solution:
    def _removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return len(nums)

        i = 1
        while i < len(nums):
            if i >= 1 and nums[i] == nums[i-1]:
                del nums[i-1]
                i -= 1

            i +=1

        return len(nums)

    def _removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return len(nums)

        lower = 0
        upper = 1
        while lower < len(nums):
            while upper < len(nums) and nums[lower] == nums[upper]:
                upper += 1
                
            del nums[lower + 1:upper]
            lower += 1
            upper = lower + 1

        return len(nums)
    
    def _removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return len(nums)

        insertion_idx = 0

        for idx,_ in enumerate(nums):
            if not nums[idx] == nums[insertion_idx]:
                nums[insertion_idx + 1] = nums[idx]
                insertion_idx += 1

        #del nums[insertion_idx + 1:]
        return insertion_idx + 1

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = list(set(nums))
        s.sort()
        l = len(s)
        nums[0:l] = s
        
        return l
    

test = [1,1,2,2,3,4,4]
#test=[]
s = Solution()
print(s.removeDuplicates(test))
print(test)
            
