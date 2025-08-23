# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node, lowerBound, upperBound):
            if node == None:
                return True
            
            if lowerBound != None and node.val <= lowerBound:
                return False
          
            
            if upperBound != None and node.val >= upperBound:
                return False

            return check(node.left, lowerBound, node.val) and check(node.right, node.val, upperBound)
        
        return check(root, None, None)