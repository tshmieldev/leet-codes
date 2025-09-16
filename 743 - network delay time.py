class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        graph = defaultdict(lambda: [])

        for src, dest, weight in times:
            graph[src].append((dest, weight))
        

        # do djikstra on graph from k
        dist = { node: float('inf') for node in range(1, n+1) }
        dist[k] = 0

        pq = [(0, k)]

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue # outdated entry, caused by using heappush instead of decreasekey
            for v,w in graph[u]:
                if d + w < dist[v]:
                    # relax
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

        maxval = max(dist.values())
        return -1 if maxval == float('inf') else maxval