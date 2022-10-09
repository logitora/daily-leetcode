"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height) - 1
        i = 0
        area = 0
        while i < n:
            l = n - i
            w = min(height[i], height[n])
            area = max(area, w*l)
            if height[i] < height[n]:
                i += 1
            else:
                n -= 1
        return area
"""
Two pointers method, one on the left end of the array (i) and the other on the right end of the array (n)
Bring the pointers closer, keeping track of the area between the two pointers.
The height of the box will always be the minimum col height between the two of height[i] and height[n]
Width of the box is just the index distance between the two pointers
Keep track of the biggest area we encounter, so we only want to replace the area value if w*l is greater than the previous area value that we recorded
Lastly, we want to "get rid of" the smaller of the two heights and keep the bigger column or end. If the left col was shorter than the right, increment left pointer and vice versa
Doing this, we hope to find another column that is taller and hopefully leads to a bigger area.

Time = O(n) linear. Increment through the array once 
Space = O(1) no additional arrays needed to be created
"""