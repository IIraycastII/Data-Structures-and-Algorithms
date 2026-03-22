class Solution(object):
    def canAliceWin(self, nums):
        single_digit = []
        double_digit = []

        for i in nums:
            if len(str(i)) == 1:
                single_digit.append(i)
            elif len(str(i)) == 2:
                double_digit.append(i)
        
        if sum(single_digit) > sum(double_digit) or sum(single_digit) < sum(double_digit):
            return True
        else:
            return False