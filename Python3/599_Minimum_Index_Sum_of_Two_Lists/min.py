class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = {s: idx for (idx,s) in enumerate(list1)}
        d2 = {s: idx for (idx,s) in enumerate(list2)}

        min_sum = float('inf')
        results = []
        
        for s in d1:
            if s in d2:
                c_sum = d1[s] + d2[s]
                if c_sum < min_sum:
                    results = [s]
                    min_sum = c_sum
                elif c_sum == min_sum:
                    results.append(s)
        return results
                

        

        return results
