class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum_1 = numbers[left] + numbers[right]
            if sum_1 == target:
                return [left + 1, right + 1]
            elif sum_1 > target:
                right -= 1
            elif sum_1 < target:
                left += 1
        return 0