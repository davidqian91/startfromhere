class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        paths = [[0 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            paths[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                paths[i][0] = paths[i-1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                paths[0][j] = paths[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m-1][n-1]

s = Solution()
grid = [[1, 0]]
print(s.uniquePathsWithObstacles(grid))
