from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        in_degrees = {}

        graph = {}

        for pre in prerequisites:
            in_degrees[pre[0]] = in_degrees.get(pre[0],0) + 1
            in_degrees[pre[1]] = in_degrees.get(pre[1],0)
            if pre[1] in graph:
                graph[pre[1]].add(pre[0])
            else:
                graph[pre[1]] = set() 
                graph[pre[1]].add(pre[0])

        queue = deque()
        courses_taken = numCourses - len(in_degrees.keys()) # weird task requirement
        for node, degree in in_degrees.items():
            if degree == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            out = graph.get(node, None)
            courses_taken += 1
            if out == None:
                continue
            for el in out:
                in_degrees[el] -= 1
                if in_degrees[el] == 0:
                    queue.append(el)
        return courses_taken == numCourses

s = Solution()

print(s.canFinish(3, [[1,4],[2,4],[3,1],[3,2]]))