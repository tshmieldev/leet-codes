class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(s)+1):
            if s[i-1] in '123456789':
                dp[i] += dp[i-1]
            if 9 < int(s[i-2] + s[i-1]) < 27:
                dp[i] += dp[i-2]
            
        return dp[-1]

S = Solution()