class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        
        q = deque([(id, 0)]) #id, level
        visited = set([id])
        vids = {}
        while q:
            node, depth = q.popleft()
            
            if depth == level:
                for vid in watchedVideos[node]:
                    vids[vid] = vids.get(vid, 0) + 1
                continue
            
            for neighbor in friends[node]:
                if neighbor in visited:
                    continue
                q.append((neighbor, depth+1))
                visited.add(neighbor)
        
        arr = []

        for key, value in vids.items():
            arr.append((value, key)) # Tuple used for sorting convenience
        arr.sort()

        arr = [x[1] for x in arr]
        return arr