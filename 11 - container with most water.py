class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxarea = 0
        areal = 0
        arear = len(height) - 1

        l = 0
        r = len(height) - 1

        while l < r:
            thisarea = min(height[l], height[r]) * (r-l)

            if thisarea > maxarea:
                maxarea = thisarea
                areal = l
                arear = r
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxarea