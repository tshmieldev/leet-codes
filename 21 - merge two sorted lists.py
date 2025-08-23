class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None
        current = None

        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            current = head = list1
            list1 = list1.next
        else:
            current = head = list2
            list2 = list2.next
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            else:
                current.next = list2
                list2 = list2.next
                current = current.next
        
        while list1:
            current.next = list1
            list1 = list1.next
            current = current.next
        while list2:
            current.next = list2
            list2 = list2.next
            current = current.next 

        return head

s = Solution()

print(s.mergeTwoLists(ListNode(1, ListNode(2, ListNode(3, None))),ListNode(1, ListNode(3, ListNode(4, None)))))