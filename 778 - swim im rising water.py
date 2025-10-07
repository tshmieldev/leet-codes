class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [(grid[0][0], 0, 0)] # dist, row, col
        visited = [[False] * n for _ in range(n)]
        while q:
            dst, r, c = heappop(q)
            r = -r
            c = -c
            if visited[r][c]:
                continue
            visited[r][c] = True
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for d in dirs:
                newr, newc = r + d[0], c + d[1]
                if 0 <= newr < n and 0 <= newc < n:
                    heappush(q, (max(dst, grid[newr][newc]), -newr, -newc)) 
            if r == c == n-1:
                return dst
        return -1