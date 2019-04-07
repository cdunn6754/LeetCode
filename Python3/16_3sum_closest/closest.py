import unittest


class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        if len(nums) < 3:
            return None
        
        nums.sort()

        lower = set()
        best_diff = float('inf')
        best_result = None

        remaining = {}
        
        for n in nums:
            if remaining.get(n) == None:
                remaining[n] = 1
            else:
                remaining[n] += 1

        for n in nums[0:-1]:
            remaining[n] -= 1
            
            max_key = max([n for n in remaining if remaining[n] > 0])
            min_key = min([n for n in remaining if remaining[n] > 0])

            for ln in lower:
                needed = target - (n + ln)

                if not remaining.get(needed) == None and remaining.get(needed) > 0:
                    return n + ln + needed

                if needed < min_key:
                    diff = abs(target - (min_key + n + ln))
                    if diff < best_diff:
                        best_diff = diff
                        best_result = min_key + n + ln
                elif needed > max_key:
                    diff = abs(target - (max_key + n + ln))
                    if diff < best_diff:
                          best_diff = diff
                          best_result = max_key + n + ln

                else:
                    temp = needed
                    while temp > min_key:
                        temp -= 1
                        rem = remaining.get(temp)
                        if  not(rem == None or rem <= 0):
                            diff = abs(target - (temp + n + ln))
                            if diff < best_diff:
                                best_diff = diff
                                best_result = temp + n + ln
                            break
                    temp = needed
                    while temp < max_key:
                        temp += 1
                        rem = remaining.get(temp)
                        if  not(rem == None or rem <= 0):
                            diff = abs(target - (temp + n + ln))
                            if diff < best_diff:
                                best_diff = diff
                                best_result = temp + n + ln
                            break
            lower.add(n)
        return best_result

class TestClosest(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def testClosest(self):
        arr = [-1, 2, 1, -4]
        self.assertEqual(self.sol.threeSumClosest(arr, 1), 2)

        arr = [1,1,1,0]
        self.assertEqual(self.sol.threeSumClosest(arr, -100), 2)

        arr = [1,2,5,10,11]
        self.assertEqual(self.sol.threeSumClosest(arr, 12), 13)

        arr = [1,6,9,14,16,70]
        self.assertEqual(self.sol.threeSumClosest(arr, 81), 80)

if __name__ == "__main__":
    unittest.main()
