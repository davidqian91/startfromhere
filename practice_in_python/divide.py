class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 0
        sign = 1
        if dividend < 0:
            dividend = 0 - dividend
            sign = 0-sign
        if divisor < 0:
            divisor = 0 - divisor
            sign = 0 - sign
        if dividend < divisor:
            return 0
        p = 1
        t = p*divisor
        while dividend > 10 * t:
            p *= 10
            t *= 10
        res = 0
        while p > 0:
            while dividend >= t:
                dividend -= t
                res += p
            p /= 10
            t /= 10
        return res

s = Solution()
print(s.divide(78123213, 23))
