class Solution(object):
    def intersection(self, nums1, nums2):
        list_1 = []
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        for i in nums1:
            if i in nums2:
                list_1.append(i)
        
        return list_1