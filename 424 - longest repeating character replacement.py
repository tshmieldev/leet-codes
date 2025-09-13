class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        A = [0] * 26
        l = 0
        mx = 1
        currentmax = 0
        
        for r in range(len(s)):
            A[ord(s[r]) - ord('A')] += 1
            currentmax = max(currentmax, A[ord(s[r]) - ord('A')])
            if (r-l+1) - currentmax > k:
                A[ord(s[l]) - ord('A')] -= 1
                l += 1
            else:
                mx = max(mx, (r-l+1))
        return mx
        