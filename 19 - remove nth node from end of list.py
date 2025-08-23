class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """



        counter = 0

        fast = head
        slow = head

        while fast.next:
            fast = fast.next
            counter += 1
            if counter > n:
                slow = slow.next

        length = counter + 1 

        if n == length:
            return head.next

        slow.next = slow.next.next
        return head
        