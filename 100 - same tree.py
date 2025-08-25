class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if bool(p) != bool(q):
            return False
        # same as not p or q, guaranteed by the check above
        if not p:
            return True        

        q = deque([(p, q)])

        while q:
            (n1, n2) = q.popleft()
            
            # same as not n1 or n2, as guaranteed by inserting nodes that have the same bool value
            if not n1:
                continue

            if n1.val != n2.val:
                return False
            
            if bool(n1.left) != bool(n2.left) or bool(n1.right) != bool(n2.right):
                return False
            
            q.append((n1.left, n2.left))
            q.append((n1.right, n2.right))
            
        return True