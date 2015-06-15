class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        up = self.bsRoundUp(nums, 0, len(nums)-1, target)
        down = self.bsRoundDown(nums, 0, len(nums)-1, target)
        if up == 0:
            return [-1, -1]
        elif down == len(nums)-1:
            return [-1, -1]
        if down + 1 > up -1:
            return [-1, -1]
        return [down+1, up-1]

    def bsRoundUp(self, nums, p, q, target):
        if p == q:
            if nums[p] <= target:
                return p+1
            else:
                return p
        r = p + (q-p)/2
        if nums[r] > target:
            return self.bsRoundUp(nums, p, r, target)
        else:
            return self.bsRoundUp(nums, r+1, q, target)

    def bsRoundDown(self, nums, p, q, target):
        if p == q:
            if nums[p] < target:
                return p
            else:
                return p-1
        r = p + (q-p)/2
        if nums[r] >= target:
            return self.bsRoundDown(nums, p, r, target)
        else:
            return self.bsRoundDown(nums, r+1, q, target)

    # def bsRoundDown(self, 
s = Solution()
nums = [1,2,3,8,8,8,8,9]
print(s.searchRange(nums, 3))
