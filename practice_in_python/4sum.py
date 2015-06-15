class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
        

    def threeSum(self, num, sum, f):
        s = num
        sol = []
        for i in range(len(s) - 2):
            if i == 0 or s[i] != s[i-1]:
                target = sum - s[i]
                l = i + 1
                h = len(s) - 1
                while(l < h):
                    res = s[l] + s[h]
                    if res == target:
                        sol.append(list((f, s[i], s[l], s[h])))
                        while l < h and s[l] == s[l+1]:
                            l += 1
                        while l < h and s[h] == s[h-1]:
                            h -= 1
                        l += 1
                        h -= 1
                    elif res > target:
                        h -= 1
                    else:
                        l += 1
        return sol

s = Solution()
nums = [-1,-5,-5,-3,2,5,0,4]
s.fourSum(nums, -7)
