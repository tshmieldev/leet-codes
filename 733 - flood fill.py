class Solution(object):
    def floodFill(self, image, sr, sc, color, floodColor=None):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if floodColor == None:
            floodColor = image[sr][sc]
        if floodColor == color:
            return image # tricky data, avoid infinite loop
        image[sr][sc] = color

        if sc+1 < len(image[0]) and image[sr][sc+1] == floodColor:
            self.floodFill(image, sr, sc+1, color, floodColor)
        if sc-1 >= 0 and image[sr][sc-1] == floodColor:
            self.floodFill(image, sr, sc-1, color, floodColor) 
        if sr+1 < len(image) and image[sr+1][sc] == floodColor:
            self.floodFill(image, sr+1, sc, color, floodColor)
        if sr-1 >= 0 and image[sr-1][sc] == floodColor:
            self.floodFill(image, sr-1, sc, color, floodColor)
        
        return image