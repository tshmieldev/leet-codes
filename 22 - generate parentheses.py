class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res, sol = [], []


        def backtrack(l, r):
            if l + r == 2 * n:
                res.append(''.join(sol))
                return
            if l < n:
                sol.append('(')
                backtrack(l+1, r)
                sol.pop()
            if l > r:
                sol.append(')')
                backtrack(l, r+1)
                sol.pop()
        backtrack(0, 0)
        return res