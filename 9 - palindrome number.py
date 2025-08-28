class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        xc = x
        r = 0
        while xc > 0:
            r *= 10
            r += xc % 10
            xc //= 10
            

        return r == x 