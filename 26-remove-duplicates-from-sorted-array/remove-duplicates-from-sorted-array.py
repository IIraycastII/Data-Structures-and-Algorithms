class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        right = left + 1
        

        while right < len(nums):
            if nums[left] == nums[right]:
                nums.remove(nums[right])
            elif nums[left] != nums[right]:
                left += 1
                right += 1
        
        return len(nums)
