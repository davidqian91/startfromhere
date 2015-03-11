class Solution:
    # divide and conquer
    # find the maximum profit should require us to find the max price difference
    # create a difference price list
    # find the max subarrays in the list
    # use divid and conquer
    # there's three situation of the original problem
    # 1. the max subarrays are all in the left part of the orginal list
    # 2. ... right part
    # 3. part in the left and part in the right
    # solve 1 and 2 recursively
    # solve 3 by find the max subarrays starting from the median
    # @return an integer as the maximum profit
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        profit = []
        profit.append(0)
        for i in range(1, len(prices), 1):
            profit.append(prices[i] - prices[i-1])
        return self.dcProfit(profit, 0, len(profit)-1)

    def dcProfit(self, profit, p, q):
        if q == p:
            return 0
        r = (p + q) / 2
        p1 = self.dcProfit(profit, p, r)
        p2 = self.dcProfit(profit, r+1, q)
        m1 = 0
        sum = 0
        for i in range(r, p-1, -1):
            sum += profit[i]
            if sum > m1:
                m1 = sum
        m2 = 0
        sum = 0
        for i in range(r+1, q+1, 1):
            sum += profit[i]
            if sum > m2:
                m2 = sum
        p3 = m1 + m2
        return max(p1, p2, p3)

s = Solution()
prices = [2,1,2,0,1]
print(s.maxProfit(prices))
