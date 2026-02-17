class Solution(object):
    def addToArrayForm(self, num, k):
        a = ''
        list_1 = []

        for i in num:
            a += str(i)
        
        sum_1 = int(a) + k

        for i in str(sum_1):
            list_1.append(int(i))
        return list_1

        