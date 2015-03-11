class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate1(self, nums, k):
        l = len(nums)-1
        for i in range(k):
            tmp = nums.pop(l)
            nums.insert(0, tmp)

    def rotate(self, nums, k):
        l = len(nums)
        l1 = nums[0:l-k]
        print(l1)
        l2 = nums[l-k:l]
        print(l2)
        nums = l2 + l1
        print(nums)

s = Solution()
nums = [1, 2, 3]
s.rotate(nums, 1)
print(nums)
