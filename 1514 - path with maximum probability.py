class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        
        graph = { x : [] for x in range(n) }

        for i in range(len(succProb)):
            src, dest = edges[i]
            w = succProb[i]

            graph[src].append((dest, w))
            graph[dest].append((src, w))

        dist = { x: 0 for x in range(n) }

        dist[start_node] = 1

        pq = [(-1, start_node)]

        while pq:
            d, node = heapq.heappop(pq)
            d = -d
            if node == end_node:
                return d
            if d != dist[node]:
                continue
            for n, w in graph[node]:
                if d * w > dist[n]:
                    dist[n] = d * w
                    heapq.heappush(pq, (-d*w, n))
        
        return dist[end_node]