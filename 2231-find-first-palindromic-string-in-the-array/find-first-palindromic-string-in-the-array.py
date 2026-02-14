class Solution(object):
    def firstPalindrome(self, words):
        validate = 0
        for i in words:
            if i == i[::-1]:
                validate = 1
                return i
                break
            if i != i[::-1]:
                validate = 0
        
        if validate == 0:
            return ""


        