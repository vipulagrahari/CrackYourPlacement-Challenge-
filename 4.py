
# 73. Set Matrix Zeroes
# Medium

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        itracker = []
        jtracker = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == 0):
                    itracker.append(i)
                    jtracker.append(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i in set(itracker) or j in set(jtracker)):
                    matrix[i][j] = 0
        