class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []

        def backtrack(i):
            sol.append(candidates[i])
            if sum(sol) == target:
                res.append(sol[:])
                sol.pop()
                return
            for x in range(i, len(candidates)):
                if sum(sol) + candidates[x] <= target:
                    backtrack(x)
            sol.pop()
        
        for i in range(len(candidates)):
            backtrack(i)

        return res