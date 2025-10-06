from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:

        c = 1
        ptr = 0
        for i in range(1, len(chars)+1):
            if i == len(chars) or chars[i] != chars[i-1]:
                chars[ptr] = chars[i-1]
                ptr += 1
                if c > 1:
                    for d in str(c):
                        chars[ptr] = d    
                        ptr += 1
                c = 1
            else:
               c += 1
        return ptr

S = Solution()
print(S.compress(["a","a", 'a', "b","b","a","a"]))