class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def vcount(st):
            c = 0
            for ch in st:
                if ch in 'aeiou':
                    c += 1
            return c
        
        while s:
            # Alice turn
            vcs = vcount(s)
            if vcs == 0:
                return False
            if vcs % 2 and s[0] in 'aeiou' and s[-1] in 'aeiou':
                return True
            bestlen = 0
            bi = -1
            bj = -1
            # Alice move
            for i in range(len(s)):
                for j in range(len(s) - 1, i - 1, -1):
                    tmp = vcount(s[i:j+1])
                    if tmp % 2 and (1 + j - i) > bestlen:
                        bestlen = 1 + j - i
                        bi = i
                        bj = j
                        break
                if bestlen:
                    break
            if bestlen == 0:
                return False
            s = s[:bi] + s[bj+1:]
            # Bob turn

            if len(s) == 0 or len(s) == 1 and vcount(s) == 1:
                return True
            
            # Bob move
            bestlen = 0
            bi = -1
            bj = -1
            for i in range(len(s)):
                for j in range(len(s) - 1, i - 1, -1):
                    tmp = vcount(s[i:j+1])
                    if (not (tmp % 2)) and (1 + j - i) > bestlen:
                        bestlen = 1 + j - i
                        bi = i
                        bj = j
                        break
                if bestlen:
                    break
            if bestlen == 0:
                return False
            s = s[:bi] + s[bj+1:]
        return False