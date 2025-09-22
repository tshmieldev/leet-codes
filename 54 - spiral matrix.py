from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        res = [0] * (m*n)
        leftbound = 0
        rightbound = n-1
        topbound = 0
        bottombound = m-1
        direction = (0, 1)
        coords = (0, 0)
        for i in range(m*n):
            res[i] = matrix[coords[0]][coords[1]]
            
            candidate = (coords[0] + direction[0], coords[1] + direction[1])

            if topbound <= candidate[0] <= bottombound and leftbound <= candidate[1] <= rightbound:
                coords = candidate
                continue

            # else: need to change direction, and update bounds.
            if direction == (0, 1):
                # now go down
                direction = (1, 0)
                topbound += 1
            elif direction == (0, -1):
                # now go up
                direction = (-1, 0)
                bottombound -= 1
            elif direction == (1, 0):
                # go left
                direction = (0, -1)
                rightbound -= 1
            else:
                # go right
                direction = (0, 1)
                leftbound += 1
            
            coords = (coords[0] + direction[0], coords[1] + direction[1])
        
        return res