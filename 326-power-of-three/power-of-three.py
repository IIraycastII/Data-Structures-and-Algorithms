class Solution(object):
    def isPowerOfThree(self, n):
        a = 0
        b = 3

        while True:
            a += 1
            c = b ** a

            if c == n or n == 1:
                return True
                break
            elif c > n or n == -1:
                return False
                break

            c = 0