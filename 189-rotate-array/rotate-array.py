class Solution(object):
    def rotate(self, nums, k):
        if k <= len(nums):
            nums_2 = nums[-k:]
            del nums[-k:]
            nums_2.extend(nums)

            nums[:] = nums_2

            return nums
        elif k > len(nums):
            k %= len(nums)
            nums_2 = nums[-k:]
            del nums[-k:]
            nums_2.extend(nums)

            nums[:] = nums_2

            return nums