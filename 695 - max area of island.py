class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        res = 0 

        def dfs(r, c):
            ROWS, COLS = len(grid), len(grid[0])
            if r < 0 or r == ROWS:
                return 0
            if c < 0 or c == COLS:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
      
            return 1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    res = max(res, dfs(r,c))
        
        return res