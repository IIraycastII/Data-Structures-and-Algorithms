class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) != 1:
            for i in nums:
                if i == 0:
                    nums.remove(i)
                    nums.insert(len(nums), 0)
            return nums
        else:
            return nums