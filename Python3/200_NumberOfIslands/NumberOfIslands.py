import unittest

class Solution:
    def __init__(self, grid=None):
        self.grid=grid

    def in_grid(self, point):
        if point[0] < 0 or point[0] >= len(self.grid):
            return False
        if point[1] < 0 or point[1] >= len(self.grid[0]):
            return False
        return True
    
    def is_water(self, point):
        return not self.in_grid(point) or self.grid[point[0]][point[1]] == "0"

    def get_next_point(self, point):
        if not self.in_grid(point):
            return None
        
        if point[1] < len(self.grid[0]) - 1:
            return (point[0], point[1] + 1)
        elif point[0] < len(self.grid) - 1:
            return (point[0] + 1, 0)
        else:
            return None

    def visit_island(self, point, point_island, island):
        if self.is_water(point) or not point_island.get(point) == None:
            return None

        island.append(point)
        point_island[point] = island

        self.visit_island((point[0] + 1, point[1]), point_island, island)
        self.visit_island((point[0] - 1, point[1]), point_island, island)
        self.visit_island((point[0], point[1] + 1), point_island, island)
        self.visit_island((point[0], point[1] - 1), point_island, island)
        
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        self.grid = grid
        num_islands = 0
        point_island = {}

        for i, _ in enumerate(self.grid):
            for j, _ in enumerate(self.grid[0]):
                point_val = self.grid[i][j]
                point = (i,j)
                
                if point_island.get(point) != None or point_val == "0":
                    continue
                new_island = []
                num_islands += 1
                self.visit_island(point, point_island, new_island)

        return num_islands
                
        

class MainTest(unittest.TestCase):

    def setUp(self):
        self.grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]

        self.grid2 = [
            ["0", "0"],
            ["0", "0"]
        ]

        self.sol = Solution(grid=self.grid)

    # def test_is_water(self):
    #     self.assertFalse(self.sol.is_water((0,0)))
    #     self.assertTrue(self.sol.is_water((0,4)))
    #     self.assertTrue(self.sol.is_water((3,0)))

    def test_get_next_point(self):
        self.assertEqual(self.sol.get_next_point((0,0)), (0,1))
        self.assertEqual(self.sol.get_next_point((0,4)), (1,0))
        self.assertIsNone(self.sol.get_next_point((3,4)))
        
    def test_integration(self):
        #num = self.sol.numIslands(self.grid)
        #self.assertEqual(num, 1)
        num2 = self.sol.numIslands(self.grid2)
        self.assertEqual(num2, 0)

if __name__ == "__main__":
    unittest.main()
        
