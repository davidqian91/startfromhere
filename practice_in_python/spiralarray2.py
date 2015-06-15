class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        def spriralRecur(matrix, l, num, n):
            if l > (n+1)/2:
                return
            if n == 2 * l:
                matrix[l][l] = num
                return
            for i in range(l, n-l):
                matrix[l][i] = num
                num += 1
            for i in range(l, n-l):
                matrix[i][n-l] = num
                num += 1
            for i in range(n-l, l, -1):
                matrix[n-l][i] = num
                num += 1
            for i in range(n-l, l, -1):
                matrix[i][l] = num
                num += 1
            spriralRecur(matrix, l+1, num, n)

        matrix = [[1 for i in range(n)] for j in range(n)]
        spriralRecur(matrix, 0, 1, n - 1)
        return matrix

s = Solution()
print(s.generateMatrix(2))
