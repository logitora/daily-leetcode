"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.
"""
def search(board, row, col, word, visited, pos=0):
    if pos == len(word):
        return True
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or visited[row][col] == True or board[row][col] != word[pos]:
        return False

    visited[row][col] = True
    res = search(board, row+1, col, word, visited, pos+1) or search(board, row-1, col, word, visited, pos+1) or search(board, row, col+1, word, visited, pos+1) or search(board, row, col-1, word, visited, pos+1)
    visited[row][col] = False
    return res

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                if search(board, row, col, word, visited):
                    return True
        return False
"""
DFS solution to find the word of interest. Create a visited matrix to keep track of the cells that we have visited while searching for the next letter. Switch it back to False
when a new start point is established and search is initiated again. 
Nested for loop to iterate through the entire matrix. A helper function was also established to perform the DFS with a new variable, pos. Pos will indicate which
index in word we are looking at. Check to see if pos == len(word) or if the next cell of interest is within the bounds of the matrix.
Mark cell as visited and then initiate DFS and incrementing pos every call. If none of these options return a result, mark everything that was True in visited back to False, 
and try again at a new cell that matches word[0].
Time = O(mn4^w) where w = len(word). mn for each cell in the matrix, 4 for each direction that we are checking. 
Space = O(mn) for the visited matrix
"""