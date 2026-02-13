class Solution(object):
    def sortArrayByParity(self, nums):
        list_1 = []

        for i in nums:
            if i % 2 == 0:
                list_1.insert(0, i)
            if i % 2 != 0:
                list_1.append(i)

        return list_1