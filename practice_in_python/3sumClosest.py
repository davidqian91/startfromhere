class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if len(nums) < 3:
            return None
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[j] + nums[k] + nums[i]
                if s == target:
                    return target
                if abs(res - target) > abs(s - target):
                    res = s
                if s > target:
                    k -= 1
                else:
                    j += 1
        return res

s = Solution()
nums = [1,-3,3,5,4,1]
print(s.threeSumClosest(nums, 1))