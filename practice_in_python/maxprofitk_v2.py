import heapq


class Solution:
    # @return an integer as the maximum profit
    def maxProfit(self, k, prices):
        if len(prices) < 2 or k <= 0:
            return 0
        v = prices[0]
        p = prices[0]
        s = []
        d = []
        for i in range(1, len(prices)+1, 1):
            if i != len(prices) and prices[i] >= prices[i-1]:
                continue
            p = prices[i-1]
            if v < p:
                if s:
                    (x, y) = s[len(s)-1]
                    if x <= v and y <= p:
                        s.pop()
                        d.pop()
                        s.append((v, y))
                        d.append(y-v)
                        s.append((x, p))
                        d.append(p-x)
                    else:
                        s.append((v, p))
                        d.append(p-v)
                else:
                    s.append((v, p))
                    d.append(p - v)
            if i != len(prices):
                v = prices[i]
        print(s)
        print(d)
        list = heapq.nlargest(k, d)
        sum = 0
        for i in list:
            sum += i
        return sum

s = Solution()
prices = [2,6,8,7,8,7,9,4,1,2,4,5,8]
k = 2
print(s.maxProfit(k, prices))
