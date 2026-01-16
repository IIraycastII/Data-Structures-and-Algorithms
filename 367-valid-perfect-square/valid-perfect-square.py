class Solution(object):
    def isPerfectSquare(self, num):
        n = 0
        a = 0
        while True:
            n = a * a
            if n == num:
                return True
                break
            elif n > num:
                return False
                break

            a += 1
