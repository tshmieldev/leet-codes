class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l, lval, lstart = 0, 0, None
        r, rval, rstart = 0, 0, None
        
        while l < len(version1) and version1[l] != '.':
            if version1[l] == '0' and lval == 0:
                l += 1
                continue
            if lstart is None:
                lstart = l
            lval *= 10
            lval += int(version1[l])
            l += 1
        
        while r < len(version2) and version2[r] != '.':
            if version2[r] == '0' and rval == 0:
                r += 1
                continue
            if rstart is None:
                rstart = r
            rval *= 10
            rval += int(version2[r])
            r += 1
        ll = l - lstart
        rr = r - rstart
        if ll > rr:
            for _ in range(ll-rr):
                rval *= 10
        if ll < rr:
            for _ in range(rr-ll):
                lval *= 10
        
        if lval == rval:
            if l < len(version1) - 1 or r < len(version2) - 1:
                return self.compareVersion(version1[l+1:], version2[r+1:])
            return 0
        if lval > rval:
            return -1
        return 1