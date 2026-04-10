class Solution(object):
    def removeElement(self, nums, val):
        a = 0

        if len(nums) >= 1:    
            while True:
                if nums[a] == val:
                    nums.remove(nums[a])
                elif nums[a] != val:
                    a += 1
                if a == len(nums):
                    break

            return len(nums)
        return 0