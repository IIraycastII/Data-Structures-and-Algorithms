class Solution(object):
    def isPowerOfTwo(self, n):
        a = 0
        while True:
            calc = 2 ** a

            if calc == n:
                return True
                break
            elif calc > n:
                return False
                break
            
            a += 1
            