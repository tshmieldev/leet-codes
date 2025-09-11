class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vidx = []
        v = []
        for i in range(len(s)):
            c = s[i]
            if c in 'AEIOUaeiou':
                vidx.append(i)
                v.append(c)
        
        v.sort()
        it = iter(v)
        for i in vidx:
            nv = next(it)
            s[i] = nv
        
        return ''.join(s)