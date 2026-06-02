class Solution(object):
    def findTheDifference(self, s, t):
        pointer_1 = 0
        pointer_2 = 0

        s = sorted(s)
        t = sorted(t)

        while pointer_1 != len(s):
            if s[pointer_1] == t[pointer_2]:
                pointer_1 += 1
                pointer_2 += 1
            elif t[pointer_2] != s[pointer_1]:
                return t[pointer_2]
                break
            
        return t[-1]
            
        