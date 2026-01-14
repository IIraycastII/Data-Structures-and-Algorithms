class Solution(object):
    def findClosest(self, x, y, z):
        calc_1 = abs(z - x)
        calc_2 = abs(z - y)

        if calc_1 < calc_2:
            return 1
        elif calc_2 < calc_1:
            return 2
        elif calc_1 == calc_2:
            return 0
        