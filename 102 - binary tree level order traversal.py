# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        def bfs(node):
            queue = deque([node])
            
            levels = []
            
            while queue:
                level = []
                for _ in range(len(queue)):
                    
                    n = queue.popleft()
                    if not n:
                        continue
                
                    level.append(n.val)
                    if n.left:
                        queue.append(n.left)
                    if n.right:
                        queue.append(n.right)
                levels.append(level)
            return levels

        return bfs(root)