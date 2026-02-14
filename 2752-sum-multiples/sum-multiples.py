class Solution(object):
    def sumOfMultiples(self, n):
        sum_1 = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum_1 += i
        
        return sum_1
        