class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
       
        list_merge = []

        for i in nums1:
            list_merge.append(i)

        for j in nums2:
            list_merge.append(j)

        list_merge.sort()

        if len(list_merge) % 2 != 0:
            return (list_merge[int(round(len(list_merge) / 2))])
        elif len(list_merge) % 2 == 0:
            int_1 = float(list_merge[(len(list_merge) // 2) - 1])
            int_2 = float(list_merge[(len(list_merge) // 2)])
            return (int_1 + int_2) / 2

                