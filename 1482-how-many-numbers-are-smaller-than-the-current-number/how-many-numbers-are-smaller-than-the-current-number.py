class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = 0
        list_2 = []

        for i in nums:
            for j in nums:
                if j < i:
                    n += 1
            list_2.append(n)
            n = 0

        return list_2

        