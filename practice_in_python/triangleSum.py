class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        DP = [[] for row in range(len(triangle))]
        length = len(triangle)-1
        for i in range(length, -1, -1):
            for j in range(i+1):
                DP[i].append(triangle[i][j] + (0 if i == length else min(DP[i+1][j], DP[i+1][j+1]))
                print(i,j,DP[i][j])
        return DP[0][0]

s = Solution()
triangle = [[1],[2,3]]
print(s.minimumTotal(triangle))
