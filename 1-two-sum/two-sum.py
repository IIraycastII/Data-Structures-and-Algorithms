class Solution(object):
    def twoSum(self, nums, target):
        list_elements = []
        list_index = []

        # Collect all pairs of indices (i, k) where i != k
        for i in range(0, len(nums)):
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] == target:
                    list_index.append([i, k])

        # Only print the first found solution
        if list_index:
            return list_index[0]
        else:
            return "No solution found."

        return nums
        return list_index

