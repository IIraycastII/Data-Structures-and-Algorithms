class Solution(object):
    def rotate(self, matrix):
        a = 0
        result = []

        for _ in range(len(matrix)):
            list_1 = []
            for i in range(len(matrix) - 1, -1, -1):
                list_1.append(matrix[i][a])
            result.append(list_1)
            a += 1

        matrix[:] = result[:]
        return matrix
