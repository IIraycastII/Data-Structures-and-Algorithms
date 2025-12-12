class Solution(object):
    def isPalindrome(self, x):
        list_1 = []

        for i in str(x):
            list_1.append(i)

        list_1_reverse = list_1[::-1]

        if list_1 == list_1_reverse:
            return True
        elif list_1 != list_1_reverse:
            return False

     
                