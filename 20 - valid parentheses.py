class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        l = 0

        for char in s:
            if char in '({[':
                stack.append(char)
                l += 1
            else:
                if l == 0:
                    return False
                c = stack.pop()
                l -= 1
                if c == '(' and char != ')' or c == '{' and char != '}' or c == '[' and char != ']':
                    return False
        return l == 0