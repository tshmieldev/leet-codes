class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        ops = {
            '+': (lambda x, y: x + y),
            '-': (lambda x, y: x - y),
            '*': (lambda x, y: x * y),
            '/': (lambda x, y: int(float(x) / y))
        }


        for t in tokens:
            if t in ops:
                x = stack.pop()
                y = stack.pop()
                stack.append(ops[t](x,y))
            else:
                stack.append(int(t))
        return stack[0]
    
s = Solution()

print(s.evalRPN(["4","13","5","/","+"]))