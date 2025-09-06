class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def trav(i, j, v):
            if i < 0 or i >= m or j < 0 or j >= n or (i, j) in v or grid[i][j] == 0:
                return 0
            v.add((i, j))
            b = max(trav(i+1, j, v), trav(i, j+1, v), trav(i-1, j, v), trav(i, j-1, v))
            v.remove((i, j))
            return grid[i][j] + b
        
        maxp = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    v = set()
                    maxp = max(maxp, trav(i, j, v))
        return maxp