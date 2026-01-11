class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = 0
        list_2 = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    n += 1
            list_2.append(n)
            n = 0

        return list_2

        