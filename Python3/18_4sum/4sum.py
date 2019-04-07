class Solution:
    def fourSum(self, nums, target):
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

        lower = []
        results = set()
        
        for num in nums:
            d[num] -= 1
            for idx,ln in enumerate(lower):
                for ln2 in lower[1 + idx:]:
                    needed = target - (num + ln + ln2)
                    if needed in d and d[needed] > 0:
                        results.add((ln2, ln, num, needed))
            lower.append(num)
        return results

        
                    

                
s = Solution()

test = [1, 0, -1, 0, -2, 2]
print(s.fourSum(test, 0))

test = [0, 0, 0, 0]
print(s.fourSum(test, 0))
