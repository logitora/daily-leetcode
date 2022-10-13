"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color 
as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.
    m == image.length
    n == image[i].length
    1 <= m, n <= 50
    0 <= image[i][j], color < 216
    0 <= sr < m
    0 <= sc < n
"""
def fill(image: List[List[int]], i, j, original, color):
    if i < 0 or i >= len(image) or j < 0 or j >= len(image[i]) or image[i][j] != original:
        return
    image[i][j] = color
    fill(image, i+1, j, original, color)
    fill(image, i-1, j, original, color)
    fill(image, i, j+1, original, color)
    fill(image, i, j-1, original, color)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image            
        fill(image, sr, sc, image[sr][sc], color)
        return image        
"""
Basically how the paint bucket tool works in MS paint. If the origin pixel is already the same value as our new color, then nothing has to be done. 
However, if it's a different color, we have to check the origin's neighboring pixels to see if they fulfill the conditions.
This method uses recursion and BFS to change the values of all pixels that fulfill the condition. This BFS doesn't require a visited array, though, since 
the original conditions are enough to prevent an infinite loop.
The conditions are basically that we are looking at a pixel within the bounds of the matrix/graph and that the pixel is the same value as our origin pixel. 
For example, if our origin pixel value was 1 and we want to change the value to 4, all pixels that will be changed to 4 must have an original value of 1 prior to 
changing the value. The fill function just returns if one of these conditions are not fulfilled.
This can be solved using both BFS and DFS
Time = O(mn)
Space = O(1)
"""