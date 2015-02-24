class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0:
            return 0
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        outputStr = 0
        while x > 0:
            outputStr = outputStr*10 + x % 10
            x = x / 10
        print(sign*outputStr)

s = Solution()
s.reverse(1)