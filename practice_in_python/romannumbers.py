class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        c = [['I','X','C','M'],['V','L','D']]
        res = []
        s = 1000
        for l in range(3, -1, -1):
            if num < s:
                s /= 10
                continue
            n = int(num/s)
            if n == 9:
                res.append(c[0][l])
                res.append(c[0][l+1])
            elif n >= 5:
                if n > 5:
                    for i in (n, 5, -1):
                        res.append(c[0][l])
                res.append(c[1][l])
            elif n == 4:
                res.append(c[0][l])
                res.append(c[1][l])
            else:
                for i in range(n):
                    res.append(c[0][l])
            num -= n * s
            s /= 10
        print(res)
        return ''.join(res)

s = Solution()
print(s.intToRoman(145))
