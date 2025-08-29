# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head:
            return None
        
        # 1. find mid

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse list from middle -> frow slow
        prev = None
        curr = slow.next
        slow.next = None # disconnect both lists

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # prev is start of the reversed list
        rightref = prev
        leftref = head
        while rightref:
            lefttmp = leftref.next
            righttmp = rightref.next
            leftref.next = rightref
            rightref.next = lefttmp
            rightref = righttmp
            leftref = lefttmp
        
        return head