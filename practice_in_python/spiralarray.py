class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        return self.spiralRecur(matrix, 0, m-1, 0, n-1)

    def spiralRecur(self, matrix, x1, x2, y1, y2):
        #boundary
        if x1 > x2 or y1 > y2:
            return []
        res = []
        if x1 == x2:
            for j in range(y1, y2+1):
                res.append(matrix[x1][j])
            return res
        elif y1 == y2:
            for i in range(x1, x2+1):
                res.append(matrix[i][y1])
            return res
        #recursive
        else:
            for j in range(y1, y2):
                res.append(matrix[x1][j])
            for i in range(x1, x2):
                res.append(matrix[i][y2])
            for j in range(y2, y1, -1):
                res.append(matrix[x2][j])
            for i in range(x2, x1, -1):
                res.append(matrix[i][y1])
            res.extend(self.spiralRecur(matrix, x1+1, x2-1, y1+1, y2-1))
            return res

s = Solution()
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(s.spiralOrder(matrix))
