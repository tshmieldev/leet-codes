# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        def dfs(node, left):
            if node == None:
                return False
            
            left -= node.val

            if left == 0 and not node.left and not node.right:
                return True
            
            return dfs(node.left, left) or dfs(node.right, left)

        return dfs(root, targetSum) 