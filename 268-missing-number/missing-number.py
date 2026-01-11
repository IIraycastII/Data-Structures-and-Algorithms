class Solution(object):
    def missingNumber(self, nums):
        sum_1 = (len(nums) * (len(nums) + 1))//2
        sum_2 = sum(nums)

        return sum_1 - sum_2