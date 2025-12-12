class Solution(object):
    def plusOne(self, digits):
        num = 0
        digits_2 = []
        for i in digits:
            num = num * 10 + i

        num = num + 1

        for i in str(num):
            digits_2.append(i)

        digits_2 = list(map(int, digits_2))

        return digits_2
        