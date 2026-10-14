class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])
        
        visits = set() 
        def dfs(i, j): 
            if i >= rows or j >= cols or i< 0 or j < 0 or grid[i][j] == 0: 
                return 1
            if (i,j) in visits: 
                return 0
            visits.add((i,j)) 
            
            perim = dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1) + dfs(i, j + 1) 
            return perim 

        for i in range(len(grid)): 
            for j in range(len(grid[i])): 
                if grid[i][j]: 
                    return dfs(i, j) 
         
        return 0