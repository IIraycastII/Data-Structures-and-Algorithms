class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        dup = False

        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                dup = True
                break
            elif nums[i] != nums[i + 1]:
                dup = False
        
        return dup
            