class Solution:
    # binarySearch return the index of the target if find, if not , return -1
    def binarySearch(self, a, s, e, target):
        print(s,e,target)
        if s > e:
                return -1
        r = (s+e) /2
        if a[r] == target:
            return r
        elif a[r] > target:
            return self.binarySearch(a,s,r-1,target)
        else:
            return self.binarySearch(a,r+1,e,target)
    
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        newNum = sorted(num)
        print(newNum)
        for i in range(len(num)):
            if self.binarySearch(newNum, 0, len(newNum)-1, target-num[i]) >=0:
                print(i)
                for j in range(len(num)):
                    if num[j] == target-num[i]:
                        print(j)
                        return (i,j)
        return None

s = Solution()
print(s.twoSum([3,2,4],6))