class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1:
            return 1
        
        br = [1] * n
        tr = [0] * n

        for i in range(m - 1):
            for j in range(n-1, -1, -1):
                if j < n-1:
                    tr[j] = tr[j+1] + br[j]
                else:
                    tr[j] = 1
                br[j] = tr[j]
        return tr[0]