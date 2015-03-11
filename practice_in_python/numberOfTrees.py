class Solution:
    #P[i][j] denotes the number of BSTs using i ... j
    #P[i][j] = sum( P[i,k-1]*P[k+1,j]   k = i ... j
    # @return an integer
    def numTrees(self, n):
        P = [[1 for col in range(n+1)] for row in range(n+2)]
        for i in range(1, n+1, 1):
            for j in range(1, i+1, 1):
                if i == j:
                    P[j][i] = 1
                    continue
                sum = 0
                for k in range(j, i+1, 1):
                    sum += P[j][k-1] * P[k+1][i]
                P[j][i] = sum
        print(P)
        return P[1][n]

s = Solution()
print(s.numTrees(3))
