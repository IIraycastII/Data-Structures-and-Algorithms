class Solution(object):
    def divide(self, dividend, divisor):
        INT_MIN = 2 ** 31 - 1
        INT_MAX = -2 ** 31

        result =  int(float(dividend)/divisor)

        if result < INT_MAX:
            return INT_MAX
        elif result > INT_MIN:
            return INT_MIN
        else:
            return result