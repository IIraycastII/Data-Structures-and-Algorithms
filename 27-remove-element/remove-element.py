class Solution(object):
    def removeElement(self, nums, val):
        n = 0

        while True:
            try:
                if nums[n] == val:
                    nums.remove(nums[n])
                    n -= 1
                n += 1
            except IndexError:
                pass

            if n == len(nums):
                break

        print(nums)