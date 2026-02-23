class Solution(object):
    def merge(self, nums1, m, nums2, n):
        list_1 = []

        for i in range(m):
            list_1.append(nums1[i])
        
        for i in range(n):
            list_1.append(nums2[i])
        
        nums1[:] = list_1
        nums1.sort()

        return nums1