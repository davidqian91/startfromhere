##sort the list,
#search from small to large
#use binary search to find the target.
#basically O(n^2 log n)


class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        s = sorted(num)
        sol = []
        l = []
        #pick the first number, which should be the smallest of the three
        for i in range(len(s)-2):
            #pick the seconde number, should be the middle of the three
            for j in range(i+1, len(s)-1, 1):
            #the third number is greater than s[j]
            #if the inequation is false, can't find the third number anymore
                #stop from here, find another s[j].
                #do improve the performance
                #if drop the inequation check, get TLE.
                if s[i]+s[j] > -s[j]:
                    continue
                if self.binarySearch(s, j+1, len(s)-1, 0-s[i]-s[j]):
                    l.append((s[i], s[j], 0-s[i]-s[j]))
        for t in set(l):
            newl = []
            (a, b, c) = t
            newl.append(a)
            newl.append(b)
            newl.append(c)
            sol.append(newl)
        return sol

    # binarySearch return a boolean indicating whether the target is found
    def binarySearch(self, a, s, e, target):
        if s > e:
            return False
        r = (s+e) / 2
        if a[r] == target:
            return True
        elif a[r] > target:
            return self.binarySearch(a, s, r-1, target)
        else:
            return self.binarySearch(a, r+1, e, target)
