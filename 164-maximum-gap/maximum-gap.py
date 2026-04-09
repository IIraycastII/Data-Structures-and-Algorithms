class Solution(object):
    def maximumGap(self, nums):
        if len(nums) > 1:
            max_1 = 0
            nums.sort()

            left = 0
            right = left + 1

            while right != len(nums):
                diff = abs(nums[left] - nums[right])
                if diff > max_1:
                    max_1 = diff
                left += 1
                right += 1
            return max_1
        return 0