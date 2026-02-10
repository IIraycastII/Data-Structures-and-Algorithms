class Solution(object):
    def searchInsert(self, nums, target):
        n = 0

        for i in range(len(nums)):
            if nums[i] == target:
                print(i)
            elif nums[i] != target and n == 0:
                nums.insert(len(nums), target)
                n = 1

        nums.sort()

        return nums.index(target)
        