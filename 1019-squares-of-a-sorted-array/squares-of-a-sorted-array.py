class Solution(object):
    def sortedSquares(self, nums):
        list_1 = [i * i for i in nums]
        return sorted(list_1)
        