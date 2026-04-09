class Solution(object):
    def lengthOfLastWord(self, s):
        return len(list(s.split())[-1])