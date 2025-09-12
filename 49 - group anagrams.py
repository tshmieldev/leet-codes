class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grps = defaultdict(list)
        for an in strs:
            grps[''.join(sorted(an))].append(an)
        
        return grps.values()