class Solution(object):
    def majorityElement(self, nums):
            nums_2 = []
            nums_2[:] = list(set(nums))

            for i in range(len(nums_2)):
                if nums.count(nums_2[i]) > len(nums)//2:
                    return nums_2[i]
                    