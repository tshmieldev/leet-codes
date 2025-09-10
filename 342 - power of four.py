class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = 1

        while x <= n:
            if x == n:
                return True
            x <<= 2
        
        return False