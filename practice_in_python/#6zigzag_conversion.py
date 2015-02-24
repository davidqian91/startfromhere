class Solution:
    # @return a string
    def convert(self, s, nRows):
    	if nRows == 1: 
            return s
        queues = ["" for row in range(nRows)]
        step = 1
        level = 0
        for w in s:
            queues[level]+=w
            if level == 0:
                step = 1
            if level == nRows-1:
                step = -1
            level += step
        print("".join(queues))

s = "A"
nRows = 2
sol = Solution()
sol.convert(s,nRows)