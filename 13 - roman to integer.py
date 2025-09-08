class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        
        def getValue(char, nextChar):
            
            if char == 'I':
                if nextChar in ["V", "X"]:
                    return -1
                return 1
            
            if char == 'V':
                return 5
            
            if char == 'X':
                if nextChar in ['L', "C"]:
                    return -10
                return 10
            
            if char == 'L':
                return 50

            if char == 'C':
                if nextChar in ["D", "M"]:
                    return -100
                return 100
            
            if char == 'D':
                return 500
            
            return 1000


        for i in range(len(s)):
            char = s[i]
            nextChar = None if i == len(s)-1  else s[i+1]
            value += getValue(char, nextChar)
        
        return value