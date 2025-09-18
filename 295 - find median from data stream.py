import heapq

class MedianFinder(object):

    def __init__(self):
        self.maxh = []
        self.minh = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.maxh, -num)
        n = len(self.maxh)
        m = len(self.minh)
        while abs(n-m) > 1 or (n>0 and m>0 and -self.maxh[0] > self.minh[0]):
            while abs(n - m) > 1:
                heapq.heappush(self.minh, -heapq.heappop(self.maxh))
                n = len(self.maxh)
                m = len(self.minh)
            while -self.maxh[0] > self.minh[0]:
                heapq.heappush(self.minh, -heapq.heappop(self.maxh))
                heapq.heappush(self.maxh, -heapq.heappop(self.minh))


    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.maxh)
        m = len(self.minh)

        if n > m:
            return -self.maxh[0]
        return ( -self.maxh[0] + self.minh[0] ) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

MF = MedianFinder()
MF.addNum(1)
MF.addNum(2)
print(MF.findMedian())
MF.addNum(3)
print(MF.findMedian())