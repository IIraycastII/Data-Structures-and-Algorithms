class Solution(object):
    def removeDuplicates(self, nums):
        a = 0
        b = 0
        if len(nums) >= 3:
            while a < len(nums) - 1:
                if nums[a] == nums[a + 1] and b == 0:
                    b = 1
                    a += 1
                elif nums[a] == nums[a + 1] and b == 1:
                    nums.pop(a + 1)
                else:
                    b = 0
                    a += 1
        return len(nums)