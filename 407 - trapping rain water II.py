class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []
        R, C = len(heightMap), len(heightMap[0])
        for r in range(R):
            for c in range(C):
                if r in [0, R-1] or c in [0, C-1]:
                    heappush(heap, (heightMap[r][c],r,c))
                    heightMap[r][c] = -1
        res = 0
        maxh = -1
        while heap:
            h, r, c = heappop(heap)
            maxh = max(maxh, h)
            res += maxh-h
           
            
            dirs = [(r+1, c), (r-1, c), (r, c-1), (r,c+1)]

            for nr, nc in dirs:
                if nc == -1 or nc == C or nr == -1 or nr == R or heightMap[nr][nc] == -1:
                    continue
                heappush(heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1
        return res