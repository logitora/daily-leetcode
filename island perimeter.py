"""
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there 
is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
    row == grid.length
    col == grid[i].length
    1 <= row, col <= 100
    grid[i][j] is 0 or 1.
    There is exactly one island in grid.
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                perim += 4 * grid[i][j]
                if i > 0:
                    perim -= grid[i][j] * grid[i-1][j]
                if i < m-1:
                    perim -= grid[i][j] * grid[i+1][j]
                if j > 0:
                    perim -= grid[i][j] * grid[i][j-1]
                if j < n-1:
                    perim -= grid[i][j] * grid[i][j+1]
        return perim
"""
Iterate through the entire matrix and multiply 4 to the value of each cell. Since water cells are denoted with a 0, nothing will be 
added to our perimeter count when we encounter a water cell. However, when an island cell is encountered, 4 is added to the perimeter and some checks are done
to subtract the right amount off the perimeter count. Any side/edge of the cell that is exposed to either the edge of the matrix or to a water cell
should be counted towards the perimeter count, and any side that is adjacent to another island cell should be subtracted. The if statements are
the conditionals to be checked to see if the cell is within the bounds of the matrix and if the cell we are checking will be inside the bounds. 
If a neighboring cell is a water cell, 0 is subtracted from perimeter. If the neighboring cell is an island cell, 1 will be subtracted given that the current cell is also 
an island block. In order to check the above neighboring cell, our i iterator value must be greater than 0. To check the below neighboring cell, i cannot denote the very last row. 
The same line of thinking goes for j and checking left and right neighbors. 
Time = O(n) iterate through the whole matrix once. Checking neighbors is constant lookup time
Space = O(1)
"""