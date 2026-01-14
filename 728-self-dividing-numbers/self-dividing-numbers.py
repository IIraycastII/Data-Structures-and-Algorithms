class Solution(object):
    def selfDividingNumbers(self, left, right):
        list_1 = []

        for i in range(left, right + 1):
            is_valid = True

            for j in str(i):
                if j == "0" or i % int(j) != 0:
                    is_valid = False
                    break

            if is_valid:
                list_1.append(i)

        return list_1