
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        keys = {'p': '', 'q': ''}

        def getNodeKeys(node, p, q, key):
            if not node:
                return
            if node.val == p:
                keys['p'] = key
            if node.val == q:
                keys['q'] = key
            getNodeKeys(node.left, p, q, key + 'L')
            getNodeKeys(node.right, p, q, key + 'R')

        getNodeKeys(root, p.val, q.val, '')

      
        common = ''
        key_p = keys['p']
        key_q = keys['q']
        for i in range(min(len(key_p), len(key_q))):
            if key_p[i] == key_q[i]:
                common += key_p[i]
            else:
                break

        
        node = root
        for c in common:
            node = node.left if c == 'L' else node.right
        return node