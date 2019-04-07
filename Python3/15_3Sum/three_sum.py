class Solution:
    def _threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        d = {}

        nums.sort()

        for num in nums:
            if not d.get(num,None):
                d[num] = 1
            else:
                d[num] += 1

        lower = set()
        results = set()
        
        for idx,num in enumerate(nums):
            d[num] -= 1
            for ln in lower:
                needed = -(num + ln)
                if needed in d and d[needed] > 0:
                    results.add((ln, num, needed))
            lower.add(num)
        return results

    def threeSum(self,nums):

        nums.sort()

        
                    

                
s = Solution()

test = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(test))
