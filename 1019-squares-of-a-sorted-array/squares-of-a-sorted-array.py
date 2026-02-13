class Solution(object):
    def sortedSquares(self, nums):
        list_1 = []
        for i in nums:
            list_1.append(i ** 2)
        
        return sorted(list_1)
        