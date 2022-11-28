"""
Given an m x n matrix, return all elements of the matrix in spiral order.
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break
            
            for i in range(right-1, left-1, -1):
                res.append(matrix[i][bottom-1])
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left]):
            left += 1

        return res
"""
Pretty straightforward, our goal is to move in an inward approaching spiral of the matrix, so we will have to manipulate the constraints as we finish each row/column
in order to exclude them. Line 23 is a failsafe to terminate the loop once conditions are met to prevent double appending.

Time = O(mn)
Space = O(mn) res will be a list of all mn values in the spiral order they were appended in. 
"""