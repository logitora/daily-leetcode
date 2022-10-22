"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, 
and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above 
sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is 
less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 105
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        PAC = set()
        ATL = set()
        directions = ((1,0), (-1, 0), (0, 1), (0, -1))
        
        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            
            for direction in directions:
                next_i, next_j = i+direction[0], j+direction[1]
                if 0 <= next_i < row and 0 <= next_j < col and heights[next_i][next_j] >= heights[i][j]:
                    traverse(next_i, next_j, visited)
        
        for y in range(row):
            traverse(y, 0, PAC)
            traverse(y, col-1, ATL)
        for x in range(col):
            traverse(0, x, PAC)
            traverse(row-1, x, ATL)
        
        return list(PAC & ATL)
"""
In this method, we essentially work backwards from tiles that lead out to the ocean back to the source block. We use sets to indicate the visited cells and their
coordinates. We call traverse recursively starting from the outer edges. y = 0 and y = col-1 are the left and right edges of the matrix respectively, which touch the Pacific and 
Atlantic oceans respectively. Likewise for x = 0 and x = row-1. This will go through and mark each cell as visited if they fulfill the conditions. Since we are working backwards, we 
want to check if the next cell's value is greater than the current cell's, since water can only flow from greater to lesser values. In the end, we return any values
that the PAC and ATL sets share, indicating that those are the source blocks that flow water to both the Pacific and Atlantic. 
Time = O(mn) 
Space = O(n) two separate sets to store visited values
"""