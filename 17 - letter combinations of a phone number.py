class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mydict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res, sol = [], []
        
        if not digits:
            return []

        def backtrack(i):
            if i == len(digits):
                res.append(''.join(sol))
                return
            
            for char in mydict[digits[i]]:
                sol.append(char)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)

        return res