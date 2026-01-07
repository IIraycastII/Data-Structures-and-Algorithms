class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a = 0
        b = 0

        list_1 = []
        list_2 = []

        while a != m:
            list_1.append(nums1[a])
            a += 1

        while b != n:
            list_2.append(nums2[b])
            b += 1

        list_1.extend(list_2)
        list_1.sort()
        nums1[:] = list_1
