class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or len(strs[0]) == 0:
            return ''
        
        p = ""
        # Guaranteed to have it figured out by then or early return
        for p_i in range(len(strs[0])):
            p_c = strs[0][p_i]
            for el in strs:
                if p_i >= len(el) or not el[p_i] == p_c:
                    return p
            p += p_c
            
        return p
