class Solution:

    def is_water(self, p):
        if (
            p[1] > self.max_j or
            p[0] > self.max_i or
            p[0] < 0 or
            p[1] < 0 or
            self.grid[p[0]][p[1]] == 0
        ):
            return True
        return False

    def add_to_island(self, p, island):
        if self.is_water(p) or p in island:
            return None
        island.append(p)
        self.add_to_island((p[0], p[1]+1), island)
        self.add_to_island((p[0], p[1]-1), island)
        self.add_to_island((p[0]+1, p[1]), island)
        self.add_to_island((p[0]-1, p[1]), island)
                           
        
            
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':

        self.islands = []
        self.grid = grid
        self.max_i = len(grid) -1
        self.max_j = len(grid[0]) -1

        for i, _ in enumerate(self.grid):
            for j,_ in enumerate(self.grid[i]):
                p_val = self.grid[i][j]
                p = (i, j)

                if p_val == 1:
                    
                    # See if this p is in a known island
                    if any([p in known_island for known_island in self.islands]):
                        continue
                    new_island = []
                    self.add_to_island(p, new_island)
                    self.islands.append(new_island)

        try:
            return max([len(island) for island in self.islands])
        except ValueError:
            return 0
            
                


sol = Solution()

test = [
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0]
]

test = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(sol.maxAreaOfIsland(test))
                    
