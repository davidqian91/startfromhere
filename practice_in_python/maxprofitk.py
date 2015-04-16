class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        s = [[0 for col in range(len(prices))] for row in range(len(prices))]
        result = 0
        if (not prices) or k == 0: return result
        for i in range(len(prices)):
            result = 0
            lowest = prices[i]
            for j in range(i+1, len(prices)):
                s[i][j] = max(result, prices[j] - lowest)
                lowest = min(prices[j], lowest)
        #OPT[k,n] denotes the optimal profit gained within the first n days using k transactions. 
        OPT = [[0 for col in range(len(prices)+1)] for row in range(k+1)]
        for i in range(1,k+1,1):
            for j in range(len(prices)):
                v = OPT[i-1][j]
                for l in range(j):
                    tmp = OPT[i-1][l] + s[l+1][j]
                    if tmp>v:
                        v = tmp
                OPT[i][j] = v
        return OPT[k][len(prices)-1]

s=  Solution()
prices = [4,1,3,2,6,7]
k = 2
print(s.maxProfit(k,prices))
