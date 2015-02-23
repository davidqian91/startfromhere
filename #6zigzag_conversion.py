class Solution:
    # @return a string
    def convert(self, s, nRows):
    	queues = [[] for row in range(nRows)]
    	level = 0
    	step = 1
    	for w in s:
    		queues[level].append(w)
    		print("letter:"+w+",level:",level,",step:",step)
    		level+=step
    		if level == 0 or level == nRows-1:
    			step = -step
    	for i in range(nRows):
    		print(''.join(queues[i]))

s = "PAYPALISHIRING"
nRows = 3
sol = Solution()
sol.convert(s,nRows)