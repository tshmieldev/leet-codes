class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rottens = [] # Faster than deque in this case
        freshes = 0
        ROWS, COLS = len(grid), len(grid[0])

        def rot(r, c):
            ROWS, COLS = len(grid), len(grid[0])
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            rottens.append((r,c))
            return 1
          
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rottens.append((r, c))
                elif grid[r][c] == 1:
                    freshes += 1
        if not rottens:
            if freshes:
                return -1
            return 0

        count = 0
        while rottens and freshes:
            lr = len(rottens)
            # Simulate one turn
            for _ in range(lr):
                r, c = rottens.pop(0)
                freshes -= rot(r-1, c)
                freshes -= rot(r+1, c)
                freshes -= rot(r, c+1)
                freshes -= rot(r, c-1)
            count += 1
        
        return -1 if freshes else count