from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        # def dfs(left, right):
        #     if not left and not right:
        #         return True
        #     if not left or not right:
        #         return False
        #     return left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left)
        # return dfs(root.left, root.right)
        def bfs(node):
            queue = deque()

            queue.append((node.left, node.right))

            while(len(queue)):
                l, r = queue.popleft()
                if not l and not r:
                    continue
                if not l or not r:
                    return False
                if l.val != r.val:
                    return False
                queue.append((l.left, r.right))
                queue.append((l.right, r.left))
            return True
        pass