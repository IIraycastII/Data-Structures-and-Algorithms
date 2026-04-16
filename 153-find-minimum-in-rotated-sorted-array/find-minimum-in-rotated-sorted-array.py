class Solution(object):
    def findMin(self, nums):
        nums.sort()
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            cal = (left + right) // 2

            if nums[cal] == min(nums):
                return nums[cal]
            elif nums[cal] > min(nums):
                right = cal - 1
            else:
                left = cal + 1