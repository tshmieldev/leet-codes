class Solution:
    def decodeString(self, s: str) -> str:
        ptr = 0
        out = ''
        while ptr < len(s) and s[ptr] not in '1234567890':
            out += s[ptr]
            ptr += 1
        if ptr < len(s) - 1:
            nr = ''
            while ptr < len(s) and s[ptr] in '1234567890':
                nr += s[ptr]
                ptr += 1
            beg=ptr+1
            ptr += 12
            level = 1
            while level > 0:
                if s[ptr] == '[':
                    level += 1
                elif s[ptr] == ']':
                    level -= 1
                ptr += 1
            return out + int(nr) * self.decodeString(s[beg:ptr]) + s[ptr:]
        else:
            return out
S = Solution()
S.decodeString('3[a]2[bc]')