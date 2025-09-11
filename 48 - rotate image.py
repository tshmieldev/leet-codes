class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        layer = 0
        while layer < n // 2:
            for i in range(n-1-(layer * 2)):
                topleft = matrix[0 + layer][i + layer]
                # topright = matrix[i + x // 2][n-1 - x // 2]
                # bottomright = matrix[n-1 - x // 2][n-1-i - x // 2]
                # bottomleft = matrix[n-1-i - x // 2][0 + x // 2]
                
                matrix[0 + layer][i + layer] = matrix[n-1-i - layer][0 + layer]
                matrix[n-1-i - layer][0 + layer] = matrix[n-1 - layer][n-1-i - layer]
                matrix[n-1 - layer][n-1-i - layer] = matrix[i + layer][n-1 - layer]
                matrix[i + layer][n-1 - layer] = topleft
                
            layer += 1
            
        return matrix