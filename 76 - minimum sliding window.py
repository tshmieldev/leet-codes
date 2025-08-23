from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        def isValid(tCount, counterSum):
            if counterSum > 0:
                return False
            for c in tCount:
                if c > 0:
                    return False
            return True
        
        
        counterArray = [0] * (122 - 65 + 1)
        counterSum = len(t)

        for char in t:
            counterArray[ord(char) - 65] += 1
          

        charSet = set(t)
        candidate = ""

        l = 0
        r = -1
        while True:
            while l < len(s) and s[l] not in charSet:
                l += 1
            if l == len(s):
                return candidate

            while r < len(s) and not isValid(counterArray, counterSum):
                r += 1
                if r == len(s):
                    #end
                    return candidate
                if s[r] in charSet:
                    counterArray[ord(s[r]) - 65] -= 1
                    counterSum -= 1
            
            if r - l < len(candidate) or candidate == '':
                candidate = s[l:r+1]
            counterArray[ord(s[l]) - 65] += 1
            counterSum += 1
            l += 1
            
s = Solution()

print(s.minWindow("adobecodebanc", "abc"))