class Solution(object):
    def numberGame(self, nums):
        arr = []
        while len(nums) != 0:
            Alice = min(nums)
            nums.remove(Alice)
            Bob = min(nums)
            nums.remove(Bob)

            arr.append(Bob)
            arr.append(Alice)
        
        return arr
        