class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))] 

        dp[-1][-1] = 1

        for r in range(len(obstacleGrid)-1, -1, -1):
            for c in range(len(obstacleGrid[0])-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                    continue
                if r == len(obstacleGrid) - 1 and c == len(obstacleGrid[0]) - 1:
                    continue
                if r == len(obstacleGrid) -1:
                    dp[r][c] = dp[r][c+1]
                elif c == len(obstacleGrid[0]) -1:
                    dp[r][c] = dp[r+1][c]
                else:
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]
        
        return dp[0][0]