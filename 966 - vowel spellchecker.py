import re

class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        
        direct = set(wordlist)
        capmap = {}
        vowmap = {}
        
        def devowel(word):
            return re.sub('[aeiou]', '/', word)
        
        for word in wordlist:
            lower = word.lower()
            if lower not in capmap:
                capmap[lower] = word
            vword = devowel(lower)
            if vword not in vowmap:
                vowmap[vword] = word
        
        def match(query):
            if query in direct:
                return query
            lower = query.lower()
            if lower in capmap:
                return capmap[lower]
            vword = devowel(lower)
            if vword in vowmap:
                return vowmap[vword]
            return ""
        
        return [match(q) for q in queries]