class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                idx = i-c
                if idx < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[idx])
    
        return -1 if dp[-1] == float('inf') else dp[-1]
S = Solution()
S.coinChange([1,2,5], 11)