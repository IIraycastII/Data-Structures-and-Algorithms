class Solution(object):
    def addDigits(self, num):
        list_1 = []

        if num != 0:
            while len(str(num)) != 1:
                for i in str(num):
                    list_1.append(int(i))
                num = sum(list_1)
                list_1[:] = []

            return num
        else:
            return 0