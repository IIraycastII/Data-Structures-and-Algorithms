class Solution(object):
    def addDigits(self, num):
        if len(str(num)) != 1:
            while len(str(num)) != 1:
                a = int(num / 10)
                b = num - (int(num / 10) * 10)
                num = a + b

            return num
        elif len(str(num)) == 1:
            return num
        else:
            return 0