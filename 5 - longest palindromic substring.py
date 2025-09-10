class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = 0
        resl = 0
        resr = 0

        for i in range(len(s)):
            #odd
            c = -1
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c += 2
                l -= 1
                r += 1
            if c > res:
                res = c
                resl = l
                resr = r
            #even
            c = 0
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                c += 2
                l -= 1
                r += 1
            if c > res:
                res = c
                resl = l
                resr = r
                
        return s[resl+1:resr]