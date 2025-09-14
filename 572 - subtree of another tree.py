# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def same(n1, n2):
            if not n1 and not n2:
                return True
            
            if not n1 or not n2 or n1.val != n2.val:
                return False
            
            return same(n1.left, n2.left) and same(n1.right, n2.right)
        
        def sub(r, s):
            if r == None:
                return False
            if same(r, s):
                return True
            return sub(r.left, s) or sub(r.right, s)
        
        return sub(root, subRoot)