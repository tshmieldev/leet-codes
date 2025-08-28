# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        def dfs(node):
            if not node:
                return None
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            
            node.left, node.right = node.right, node.left

            return node
        
        return dfs(root)