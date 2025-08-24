class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = {}

        for v in range(n):
            graph[v] = set()
        
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
        

        def _dfs(graph, node, dest, visited):
            visited.add(node)

            if node == destination:
                return True

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if _dfs(graph, neighbor, dest, visited):
                        return True
            
            return False
        
        visited = set()
        
        return _dfs(graph, source, destination, visited)