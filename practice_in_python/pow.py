class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        sign = True
        if n < 0:
            n = n * (-1)
            sign = False
        res = 1
        pows = [x]
        cnt = 1
        while cnt < n:
            tmp = pows[len(pows)-1]
            pows.append(tmp*tmp)
            cnt *= 2
        cnt = 0
        while n > 0:
            if n % 2 == 1:
                res *= pows[cnt]
            n = int(n/2)
            cnt += 1
        if sign:
            return res
        else:
            return 1/res

s = Solution()
print(s.myPow(8.95371, -1))
