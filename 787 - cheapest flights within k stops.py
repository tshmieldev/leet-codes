class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        
        dist = {x: 0 if x == src else float('inf') for x in range(n)}
        tempdist = dict(dist)

        for i in range(k + 1):
            for f, t, p in flights:

                if dist[f] + p < tempdist[t]:
                    tempdist[t] = dist[f] + p
            
            for k in tempdist:
                dist[k] = tempdist[k]
            tempdist = dict(dist)
        
        return -1 if dist[dst] == float('inf') else dist[dst]