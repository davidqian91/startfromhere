class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        def rotateRecur(matrix, lower, upper):
            if lower >= upper:
                return
            for i in range(lower, upper):
                tmp = matrix[lower][i]
                matrix[lower][i] = matrix[upper + lower - i][lower]
                matrix[upper + lower - i][lower] = matrix[upper][upper + lower - i]
                matrix[upper][upper + lower - i] = matrix[i][upper]
                matrix[i][upper] = tmp
            rotateRecur(matrix, lower+1, upper-1)

        n = len(matrix)
        if n < 1:
            return
        rotateRecur(matrix, 0, n)

        