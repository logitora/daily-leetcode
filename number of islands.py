"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""
def complete_island(grid, visited, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or visited[row][col] == True or grid[row][col] == "0":
        return
    visited[row][col] = True
    
    complete_island(grid, visited, row-1, col)
    complete_island(grid, visited, row+1, col)
    complete_island(grid, visited, row, col-1)
    complete_island(grid, visited, row, col+1)
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        y, x = len(grid), len(grid[0])
        visited = [[False for i in range(x)] for j in range(y)]
        islands = 0
        for row in range(y):
            for col in range(x):
                if grid[row][col] == "1" and visited[row][col] == False:
                    islands += 1
                    complete_island(grid, visited, row, col)
        return islands
"""
Follows the same rationale/template as flood fill, but this time we will use a visited array and a nested for loop to iterate through the graph. 
The visited array will keep track of cells that we have visited in order to accurately keep track of how many islands there are. 
The purpose of the nested for loop is to iterate through the graph until we encounter the first instance of an "undiscovered" island. Iterate islands once and then 
call the complete_island recursive function to mark the whole island as visited. The conditions that must be fulfilled are all in the complete_island function.
Basically, the cell we are traversing to must be within the bounds of the matrix/graph, must be unvisited, and the value must be "1" to denote a valid island cell.
Once these conditions are fulfilled, the cell is marked as visited in the visited array.
After one round of this recursive function, the whole island should be marked and the for loop continues until another unvisited "1" cell is encountered.
This can be solved using DFS and BFS. This method was using DFS since the recursive function is taking the most recently added call from the stack
Time = O(mn)
Space = O(mn) essentially a duplicate array of the same size is made but is a bool array
"""