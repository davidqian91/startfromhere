class Solution:
    
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        return self.maxSA(A,0,len(A)-1)
    
    def maxSA(self, A, s, e):
        if s == e:
            return A[s]
        r = (s+e)/2
        max1 = self.maxSA(A,s,r)
        max2 = self.maxSA(A,r+1,e)
        max3 = self.findMaxCross(A,s,e,r)
        maxVal = max(max1,max2,max3)
        return maxVal
    
    def findMaxCross(self, A, s, e, r):
        print(s,e,r)
        leftMax = None
        rightMax = None
        sum = 0
        for i in xrange(r,s-1,-1):
            print("inxrange")
            sum += A[i]
            if leftMax is None:
                leftMax = sum
            elif sum > leftMax:
                leftMax = sum
        sum = 0
        for i in xrange(r+1,e+1,1):
            sum += A[i]
            if rightMax is None:
                rightMax = sum
            elif sum > rightMax:
                rightMax= sum
        return leftMax+rightMax


s = Solution()
A = [-2, 1]
print(s.maxSubArray(A))
