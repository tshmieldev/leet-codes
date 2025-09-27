class Solution:
    def numTilings(self, n: int) -> int:
        @lru_cache(None)
        def even(n):
            if n == 0:
                return 1
            c = 0
            c += even(n-1)
            if n-2 >= 0:
                c += even(n-2)
            c += 2 * odd(n-1)
            return c
        @lru_cache(None)
        def odd(n):
            if n <= 1:
                return 0
            if n == 2:
                return 1
            return even(n-2) + odd(n-1)
        return even(n) % (10**9+7)