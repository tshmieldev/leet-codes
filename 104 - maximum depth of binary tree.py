class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        # def bfs(node):
        #     queue = deque()
        #     queue.append((node, 1))
        #     maxDepth = 0
        #     while len(queue):
        #         (node, depth) = queue.popleft()
        #         if node:
        #             if depth > maxDepth:
        #                 maxDepth = depth
        #             queue.append((node.left, depth+1))
        #             queue.append((node.right, depth+1))
        #     return maxDepth
        
        def dfs(node):
            if not node:
                return 0
            
            return max(dfs(node.left) + 1, dfs(node.right) + 1)

        return dfs(root)