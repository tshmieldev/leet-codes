# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(l1.val + l2.val, None)
        carry = res.val // 10
        res.val %= 10
        ret = res
        while l1.next or l2.next:
            res.next = ListNode()
            res = res.next
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                res.val = l1.val + l2.val
            elif l1.next:
                l1 = l1.next
                res.val = l1.val
            else:
                l2 = l2.next
                res.val = l2.val
            res.val += carry

            carry = res.val // 10
            res.val %= 10
        
        if carry:
            res.next = ListNode(carry)

        return ret