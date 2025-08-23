class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]

            
            
            while len(stack) and temp >= stack[-1][0]:
                stack.pop()
            if len(stack) == 0:
                stack.append((temp, i))
                continue
            
            answer[i] = stack[-1][1] - i
            stack.append((temp, i))                
        
        return answer