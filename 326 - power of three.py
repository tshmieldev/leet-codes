class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n % (243 * 3 * 3) == 0:
            n /= (243 * 3 * 3)
        
        return n in [1, 3, 9, 27, 81, 243, 243*3]