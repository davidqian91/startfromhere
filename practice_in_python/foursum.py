class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        s = sorted(num)
        sol = []
        for i in range(len(s)-3):
            for j in range(i+1, len(s)-2, 1):
                if s[i] + 3*s[j] > target:
                    break
                l = j+1
                h = len(s)-1
                t = target - s[i] - s[j]
                while l < h:
                    if s[l] + s[h] == t:
                        sol.append(list((s[i], s[j], s[l], s[h])))
                        while l < h and s[l+1] == s[l]:
                            l += 1
                        while l < h and s[h-1] == s[h]:
                            h -= 1
                    elif s[l] + s[h] > t:
                        l += 1
                    else:
                        h -= 1
        return sol

s = Solution()
num = [0, 0, 0, 0]
print(s.fourSum(num, 0))
