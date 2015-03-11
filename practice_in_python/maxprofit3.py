class Solution:

    ## two situation of best profit
    # 1. best profit using one transaction and
    # the best profit of the rest of the days with another transaction
    # 2. answer of best profit with one transaction and be splited in two
    # which has more profit
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        profit = []
        profit.append(0)
        self.s = 0
        self.t = 0
        for i in range(1, len(prices), 1):
            profit.append(prices[i] - prices[i-1])
        p1 = self.dcProfit(profit, 0, len(profit)-1)
        if self.s >= self.t:
            return 0
        if self.s > 0:
            p2 = self.dcProfit(profit, 0, self.s-1)
        else:
            p2 = 0
        if self.t > 0:
            p3 = self.dcProfit(profit, self.t+1, len(prices)-1)
        else:
            p3 = 0
        negativeProfit = []
        b = False
        for i in range(self.s, self.t+1, 1):
            if profit[i] < 0:
                b = True
            negativeProfit.append(-profit[i])
        if b:
            p4 = self.dcProfit(negativeProfit, 0, len(negativeProfit)-1)
        else:
            p4 = 0
        print(p1, p2, p3, p4)
        print(self.s, self.t)
        return max(p1 + max(p2, p3), p1 + p4)

    def dcProfit(self, profit, p, q):
        if q == p:
            return 0
        r = (p + q) / 2
        p1 = self.dcProfit(profit, p, r)
        p2 = self.dcProfit(profit, r+1, q)
        m1 = 0
        sum = 0
        s = r
        for i in range(r, p-1, -1):
            sum += profit[i]
            if sum > m1:
                m1 = sum
                s = i
        m2 = 0
        sum = 0
        t = r+1
        for i in range(r+1, q+1, 1):
            sum += profit[i]
            if sum > m2:
                m2 = sum
                t = i
        p3 = m1 + m2
        m = max(p1, p2, p3)
        if p3 == m and p3 != 0:
            print(p3)
            self.s = s
            self.t = t
        return m

s = Solution()
prices = [2, 1]
print(s.maxProfit(prices))
