class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = list(OrderedDict.fromkeys(nums))
        return len(nums)