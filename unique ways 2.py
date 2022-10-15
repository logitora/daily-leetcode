"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner 
(i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.
    m == obstacleGrid.length
    n == obstacleGrid[i].length
    1 <= m, n <= 100
    obstacleGrid[i][j] is 0 or 1.
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # goal: convert obstacles from 1 to 0 and free spaces from 0 to 1
        r,c = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0] # if og value is 1, converted to 0. if free space, 1-0
        for i in range(1, r):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
        for j in range(1, c):
            obstacleGrid[0][j] = obstacleGrid[0][j-1] * (1 - obstacleGrid[0][j])
        # go through the whole matrix by columns and rows
        # multiply by (1-cell) since inner cells have not been converted like the top and left rows.
        # i.e. if cell is 1, it originally is an obstacle. 1-1 is 0 and will not contribute towards the dp sum for the next cells
        for row in range(1, r):
            for col in range(1, c):
                obstacleGrid[row][col] = (obstacleGrid[row-1][col] + obstacleGrid[row][col-1]) * (1 - obstacleGrid[row][col])
        return obstacleGrid[-1][-1]
"""
To start, obstacles are denoted as 1's and free spaces as 0. Just like in unique ways 1, we want to change the top and left edges to all 1's since the robot can 
only move down or right. Now that we have obstacles to worry about, we also have another condition to consider. If an obstacle lies in the middle of one of these edges,
every cell after that will stay 0, since the robot will not be able to go around and converge back onto that path (cannot go left or up).
Since we don't want to iterate through (0,0) twice, we change its value separately.
We perform (1-obstacleGrid[][]) in order to switch 0's to 1's and 1's to 0's. It will make the DP work easier if free spaces are denoted with 1's and obstacles with 0's.
In order to consider the edge case where there's an obstacle on one of these edges while we are switching 1's to 0's and 0's to 1's, we use the previous cell as a reference for the 
current cell's value. For example, if the previous cell was changed to a 0 (obstacle), then the current cell will be 0 since it will be multiplied by our conversion function.
Since our free space will be denoted by 1, it will not change the value when multiplied. 
Finally, just like in unique ways 1, we iterate through the "ignoring" the top and left edges. At this point, however, we still have to convert free spaces to 1's and obstacles to 0's.
We take the sum of the cells to the left and above our current cell. Then we multiply it by (1 - current cell value). We have to do this operation to convert the cell value.
We do not have to do the conversion on the neighbor sum contributing cells since we are starting at (1,1). We already took care of the whole top and left edges, so it will
work itself out as we iterate to the left and down.
Time = O(n)
Space = O(1)
"""