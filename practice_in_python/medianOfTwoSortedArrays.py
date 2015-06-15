class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        print(nums1, nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        if m == 0:
            r = int(n / 2)
            if n % 2 == 1:
                return nums2[r]
            else:
                return (nums2[r-1]+nums2[r])/2.0
        elif m == 1:
            p = nums1[0]
            r = int(n/2)
            if n == 1:
                return (p+nums2[0])/2.0
            elif n % 2 == 1:
                if p > nums2[r+1]:
                    return (nums2[r]+nums2[r+1])/2.0
                elif p < nums2[r-1]:
                    return (nums2[r-1]+nums2[r])/2.0
                else:
                    return (p+nums2[r])/2.0
            else:
                if p > nums2[r]:
                    return nums2[r]
                elif p < nums2[r-1]:
                    return nums2[r-1]
                else:
                    return p
        else:
            r1 = int(m/2)
            r2 = int(n/2)
            if m % 2 == 1 and n % 2 == 0:
        		if nums1[r1] <= nums2[r2-1]:
        			return self.findMedianSortedArrays(nums1[r1+1:], nums2[:n-r1-1])
        		elif nums1[r1] > nums2[r2]:
        			return self.findMedianSortedArrays(nums1[:r1], nums2[r1+1:])
        		else:
        			return nums1[r1]
            elif m % 2 == 0 and n % 2 == 1:
        		if nums2[r2] <= nums1[r1-1]:
        			return self.findMedianSortedArrays(nums2[r1:], nums1[:r1])
        		elif nums2[r2] > nums1[r1]:
        			return self.findMedianSortedArrays(nums2[:n-r1], nums1[r1:])
        		else:
        			return nums2[r2]
            elif m % 2 == 0 and n % 2 == 0:
        		if nums1[r1-1] > nums2[r2-1] and nums1[r1] > nums2[r2]:
        			return self.findMedianSortedArrays(nums1[:r1], nums2[r1:])
        		elif nums1[r1-1] <= nums2[r2-1] and nums1[r1] <= nums2[r2]:
        			return self.findMedianSortedArrays(nums1[r1:], nums2[:n-r1])
        		elif nums1[r1-1] > nums2[r2-1] and nums1[r1] <= nums2[r2]:
        			return (nums1[r1-1] + nums1[r1]) / 2.0
        		else:
        			return (nums2[r2-1] + nums2[r2]) / 2.0
            else:
        		if nums1[r1] < nums2[r2]:
        			return self.findMedianSortedArrays(nums1[r1:], nums2[:n-r1])
        		else:
        			return self.findMedianSortedArrays(nums1[:r1+1], nums2[r1:])
            
            # if m % 2 == 0:
            #     med1 = (nums1[r1] + nums1[r1-1])/2.0
            # else:
            #     med1 = nums1[r1]
            # if n % 2 == 0:
            #     med2 = (nums2[r2] + nums2[r2-1])/2.0
            # else:
            #     med2 = nums2[r2]
            # if med1 > med2:
            #     return self.findMedianSortedArrays(nums1[:r1], nums2[r1:])
            # else:
            #     return self.findMedianSortedArrays(nums1[r1:], nums2[:n-r1])

s = Solution()
print(s.findMedianSortedArrays([1, 2, 3, 4, 5], [4, 5, 6, 7]))
