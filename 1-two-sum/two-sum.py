class Solution(object):
    def twoSum(self, nums, target):
        nums_2 = sorted(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:
            sum_nums = nums_2[left] + nums_2[right]

            if sum_nums == target:
                first = nums.index(nums_2[left])
                if nums_2[left] == nums_2[right]:
                    second = nums.index(nums_2[right], first + 1)
                else:
                    second = nums.index(nums_2[right])
                return [first, second]
            elif sum_nums > target:
                right -= 1
            elif sum_nums < target:
                left += 1