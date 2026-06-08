class Solution(object):
    def firstMissingPositive(self, nums):
        nums = set(nums)
        a = 1
        while True:
            if a not in nums:
                return a
            a += 1