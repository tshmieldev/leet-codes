class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(heights)
        cols = len(heights[0])

        pacset, atlset = set(), set()

        def dfs(point, visited, prevHeight):
            if point in visited:
                return
            if point[0] < 0 or point[1] < 0 or point[0] == rows or point[1] == cols or heights[point[0]][point[1]] < prevHeight:
                return
            
            visited.add(point)

            dfs((point[0] + 1, point[1]), visited, heights[point[0]][point[1]])
            dfs((point[0] - 1, point[1]), visited, heights[point[0]][point[1]])
            dfs((point[0], point[1] + 1), visited, heights[point[0]][point[1]])
            dfs((point[0], point[1] - 1), visited, heights[point[0]][point[1]])
            

        for c in range(cols):
            dfs((0, c), pacset, heights[0][c])
            dfs((rows-1, c), atlset, heights[rows-1][c])
        
        for r in range(rows):
            dfs((r, 0), pacset, heights[r][0])
            dfs((r, cols-1), atlset, heights[r][cols-1])
        
        return list(pacset.intersection(atlset))