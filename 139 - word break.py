class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        lookup = {}
        def sol(i):
            if i in lookup:
                return lookup[i]
            if i == len(s):
                return True
            res = False
            for word in wordDict:
                if s[i:].startswith(word):
                    res = sol(i + len(word))
                    if res:
                        return True
            lookup[i] = False
            return lookup[i]
        
        return sol(0)