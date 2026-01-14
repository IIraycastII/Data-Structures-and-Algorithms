class Solution(object):
    def repeatedNTimes(self, nums):
        for i in range(len(nums)):
            isvalid = True
            if nums.count(nums[i]) < 2:
                isvalid = False
            
            if isvalid:
                return nums[i]
                break
            





        