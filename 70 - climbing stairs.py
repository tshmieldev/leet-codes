class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        prev = 1
        prevprev = 0

        res = 0

        for i in range(n):
            res = prev + prevprev
            prevprev = prev
            prev = res
        return res