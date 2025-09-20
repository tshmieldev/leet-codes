class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.limit = memoryLimit
        self.qlen = 0
        self.q = deque()
        self.dstmap = defaultdict(deque)
        self.dstsrcmap = defaultdict(set)
        
    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        if (timestamp, source) in self.dstsrcmap[destination]:
            return False
        if self.qlen == self.limit:
            self.forwardPacket()
        self.q.append((source,destination, timestamp))
        self.dstmap[destination].append((timestamp))
        self.dstsrcmap[destination].add((timestamp, source))
        self.qlen += 1
        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if self.q:
            p = self.q.popleft()
            src, dst, time = p
            self.dstmap[dst].popleft()
            self.dstsrcmap[dst].remove((time, src))
            self.qlen -= 1
            return [src, dst, time]
        return []

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        if not self.dstmap[destination]:
            return 0
        count = 0
        left = bisect_left(self.dstmap[destination], startTime)
        right = bisect_right(self.dstmap[destination], endTime)
        return right-left
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)