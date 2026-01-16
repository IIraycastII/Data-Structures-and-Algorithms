class Solution(object):
    def isPowerOfFour(self, n):
        calc = 0
        a = 0

        if n > 0:
            while calc <= n:
                calc = 4 ** a
                a += 1
                
                if calc == n:
                    return True
                    break
                elif calc > n:
                    return False
                    break
        else:
            return False