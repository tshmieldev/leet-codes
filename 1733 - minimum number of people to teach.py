class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        best = 500 # max m value
        
        languages = [set(language) for language in languages]

        friendships = [[f1, f2] for f1,f2 in friendships if not languages[f1-1].intersection(languages[f2-1])]

        for lang in range(1, n+1):
            thislang = 0
            langset = set()
            for f1, f2 in friendships:
                if thislang >= best:
                    break

                if lang not in languages[f1-1] and f1 not in langset:
                    thislang += 1
                    langset.add(f1)
                
                if lang not in languages[f2-1] and f2 not in langset:
                    thislang += 1
                    langset.add(f2)
                    
            best = min(best,thislang)
        
        return best