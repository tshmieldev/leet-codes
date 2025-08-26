# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        originalGraph = {}

        def dfs(node):
            if node == None:
                return

            if node.left:
                originalGraph[node].append(node.left)
                originalGraph[node.left] = [node]
            
            if node.right:
                originalGraph[node].append(node.right)
                originalGraph[node.right] = [node]

            dfs(node.left)
            dfs(node.right)
        
        originalGraph[root] = []

        dfs(root)

        # now bfs from target to level k

        q = deque([(target, 0)])
        visited = set([target])
        result = []

        while q:
            (node, level) = q.popleft()
            
            if level == k:
                result.append(node.val)
            
            for neighbor in originalGraph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, level + 1))

        return result


