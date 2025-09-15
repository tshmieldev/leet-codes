# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            if val < stack[-1].val:
                stack[-1].left = TreeNode(val)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < val:
                    last = stack.pop()
                last.right = TreeNode(val)
                stack.append(last.right)
        return root