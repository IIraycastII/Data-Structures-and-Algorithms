class Solution(object):
    def canAliceWin(self, nums):
        single_digit = []
        double_digit = []

        for i in nums:
            if i <= 9:
                single_digit.append(i)
            else:
                double_digit.append(i)
        
        if sum(single_digit) > sum(double_digit) or sum(single_digit) < sum(double_digit):
            return True
        return False