class Solution(object):
    def lengthOfLastWord(self, s):
        list_1 = list(s.split(" "))

        for i in range(len(list_1) - 1, -1, -1):
            if list_1[i] == "":
                list_1.remove(list_1[i])

        return len(list_1[len(list_1) - 1])

        