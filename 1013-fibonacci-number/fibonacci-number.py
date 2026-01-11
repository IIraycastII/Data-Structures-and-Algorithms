class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        a = 0
        b = 1

        for i in range(n - 1):
            sum_1 = a + b
            a = b
            b = sum_1

        return sum_1
        