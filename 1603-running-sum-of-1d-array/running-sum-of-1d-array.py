class Solution(object):
    def runningSum(self, nums):
        list_1 = []
        a = 0

        for i in nums:
            a += i
            list_1.append(a)
        
        return list_1