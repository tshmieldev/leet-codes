# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        dummy = ListNode()
        current = dummy
        for i, l in enumerate(lists):
            if not l:
                continue
            heapq.heappush(heap, (l.val, i, l))
            lists[i] = lists[i].next
        while heap:
            v, i, l = heapq.heappop(heap)
            current.next = l
            current = current.next
            if l.next:
                heapq.heappush(heap, (l.next.val, i, l.next))

        return dummy.next