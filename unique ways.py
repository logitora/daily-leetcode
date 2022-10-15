"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.
    1 <= m, n <= 100
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            matrix[i][0] = 1
        for j in range(n):
            matrix[0][j] = 1
        
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]
        
        return matrix[m-1][n-1]
"""
Bottom up tabulation DP.
First, we create a separate matrix of all 0's. This matrix will keep track of all the different paths that go through each cell 
and will serve as the dp addition for subsequent cells.
Then we change all the cells on the top row and left edge to 1. Since the robot can only move down or right, the cells on these edges only have one 
way to access them. For row=0, the robot can only travel right in order to access all the cells on row=0, since the robot cannot move up. The same line of thinking 
for col=0, since the robot can't move left.
Finally, we add the values of the above and left cells to get the dp value for a specific cell. We start at (1,1) to avoid an index error and since the top and left edges
should stay 1. By the time the very last cell is reached, all DP values will have been added. Return the last cell for our answer
Time = O(n)
Space = O(n)
"""