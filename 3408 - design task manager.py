class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.heap = []
        self.prios = {}
        self.idmap = {}

        for userId, taskId, priority in tasks:
            heapq.heappush(self.heap, (-priority, -taskId))
            self.prios[taskId] = priority
            self.idmap[taskId] = userId
            
    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        heapq.heappush(self.heap, (-priority, -taskId))
        self.prios[taskId] = priority
        self.idmap[taskId] = userId

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        self.add(self.idmap[taskId], taskId, newPriority)

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        self.prios[taskId] = None
        self.idmap[taskId] = None

    def execTop(self):
        """
        :rtype: int
        """
        prio, tid = None, None
        while self.heap:
            prio, tid = self.heap[0]
            prio, tid = -prio, -tid

            if prio != self.prios[tid]:
                prio, tid = None, None
                heapq.heappop(self.heap)
                continue
            break
            
        if tid is not None:
            userId = self.idmap[tid]
            self.rmv(tid)
            return userId
        else:
            return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()