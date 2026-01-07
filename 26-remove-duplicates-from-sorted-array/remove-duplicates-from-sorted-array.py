class Solution(object):
    def removeDuplicates(self, nums):
        list_2 = []

        for i in range(len(nums)):
            if nums[i] not in list_2:
                list_2.append(nums[i])
        
        nums[:] = list_2
        return len(nums)