class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        hashmap = defaultdict(deque)
        out = [-1] * len(rains)
        heap = []
        full = set()

        for day, lake in enumerate(rains):
            hashmap[lake].append(day)
        
        for i in range(len(rains)):
            lake = rains[i]
            if lake:
                if lake in full:
                    return []
                full.add(lake)
                hashmap[lake].popleft()
                if hashmap[lake]:
                    heappush(heap, hashmap[lake][0])
            else:
                if heap:
                    out[i] = rains[heappop(heap)]
                    full.remove(out[i])
                else:
                    out[i] = 1
        return out