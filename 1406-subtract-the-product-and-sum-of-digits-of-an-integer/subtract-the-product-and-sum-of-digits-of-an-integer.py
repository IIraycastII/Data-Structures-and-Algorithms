class Solution(object):
    def subtractProductAndSum(self, n):
        sum_n = 0
        mul_n = 1
        for i in str(n):
            sum_n = sum_n + int(i)
            mul_n = mul_n * int(i)

        return mul_n - sum_n
        