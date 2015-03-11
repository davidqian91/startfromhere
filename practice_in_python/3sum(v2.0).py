class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        s = sorted(num)
        sol = []
        for i in range(len(s) - 2):
            if i == 0 or s[i] != s[i-1]:
                target = 0 - s[i]
                l = i + 1
                h = len(s) - 1
                while(l < h):
                    sum = s[l] + s[h]
                    if sum == target:
                        sol.append(list((s[i], s[l], s[h])))
                        while l < h and s[l] == s[l+1]:
                            l += 1
                        while l < h and s[h] == s[h-1]:
                            h -= 1
                        l += 1
                        h -= 1
                    elif sum > target:
                        h -= 1
                    else:
                        l += 1
        return sol
