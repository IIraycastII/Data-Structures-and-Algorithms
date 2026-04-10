class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = []
        nums2[n:] = []

        for i in nums2:
            nums1.append(i)
        
        return nums1.sort()