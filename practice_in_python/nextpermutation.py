class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        i = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                break
        if i == len(nums)-1:
            swap(nums, i, i-1)
            return
        if i == 1 and nums[i-1] >= nums[i]:
            nums.sort()
            return
        for j in range(len(nums)-1, i-1, -1):
            if nums[j] > nums[i-1]:
                swap(nums, j, i-1)
                p, q = i, len(nums)-1
                while p < q:
                    swap(nums, p, q)
                    p += 1
                    q -= 1
                return

s = Solution()
nums = [1, 3, 2]
s.nextPermutation(nums)
print(nums)
