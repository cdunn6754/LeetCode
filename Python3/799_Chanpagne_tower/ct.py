import unittest

class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        cups_in_row = query_row + 1
        cups_before_row = lambda r:  (r*(r + 1))/2
        #cups_after_row = cups_before_row + cups_in_row

        if poured < 1:
            return poured
        
        rows = [ [0] * k for k in range(1, query_row+2)]

        rows[0][0] = poured

        for row_idx, row in enumerate(rows[:-1]):
            for cup_idx,into_cup in enumerate(row):
                if into_cup > 1:
                    over = into_cup - 1
                    rows[row_idx+1][cup_idx] +=  over/2
                    rows[row_idx+1][cup_idx+1] += over/2

        return min(1, rows[query_row][query_glass])
                

            

        
class ctTest(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        self.assertEqual(sol.champagneTower(1,1,1), 0)

    def test_2(self):
        sol = Solution()
        self.assertEqual(sol.champagneTower(2,1,1), 0.5)

    def test_3(self):
        sol = Solution()
        self.assertEqual(sol.champagneTower(6,2,0), 0.75)
    
unittest.main()
