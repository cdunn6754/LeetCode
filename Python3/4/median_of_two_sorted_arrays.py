class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2
        
        if not l1:
            return self.median(nums2)
        if not l2:
            return self.median(nums1)
        

        # initial guess index (in first array)
        #g = l1//2

        found = False

        while not found:
            lower = 0
            upper = len(nums1) - 1

            while lower <= upper:
                g = (lower + upper)//2
                # number of elements lower than g in nums1
                below1 = g
                # and above
                above1 = l1 - g - 1

                # Where should it be in nums2?
                below2 = (l//2) - 1 - below1
                if below2 < 0:
                    break
                
                
            

    def median(self, nums):
        l = len(nums)
        if not l%2:
            return ((nums[l//2-1] + nums[l//2])/2)
        return nums[l//2]

    def aboveAndBelow(num, nums):
        """
        Binary search on nums for num. Return number of elements above
        and below the location of num whether it exists or not.
        """
        
                
test1 = []
test2 = [3,4,5,7]
s = Solution()
print(s.median(test2))
