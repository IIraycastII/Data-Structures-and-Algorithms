class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix[0])
        n = len(matrix)

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            rows = mid // m
            column = mid % m

            value = matrix[rows][column]

            if value == target:
                return True
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1
        return False