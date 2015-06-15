class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        lastmax = nums[0]
        lastindex = 0
        nextmax = 0
        nextindex = 0
        step = 1
        for i in range(1, len(nums)):
            if lastmax < i:
                step += 1
                lastindex = nextindex
                lastmax = nextmax
                print(lastmax, lastindex)
            if nextmax < nums[i] + i:
                nextmax = nums[i] + i
                nextindex = i
        return step

s = Solution()
nums = [1,1,2,1,1]
print(s.jump(nums))
