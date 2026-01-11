class Solution(object):
    def findDisappearedNumbers(self, nums):
        list_2 = []
        n = len(nums)
        a = 0

        nums = set(nums)

        for i in range(1 + a, n + 1):
            if i not in nums:
                list_2.append(i)
            a += 1

        return list_2