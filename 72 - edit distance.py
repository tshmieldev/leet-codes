class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        dp = [[0] * (n+1) for _ in range(m+1)]

        for r in range(m+1):
            for c in range(n+1):
                if r == 0 or c == 0:
                    dp[r][c] = r + c
                else:
                    i, j = r-1, c-1
                    if word1[i] == word2[j]:
                        dp[r][c] = dp[r-1][c-1]
                    else:
                                           #Replace      #Delete     #Insert
                        dp[r][c] = 1 + min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]