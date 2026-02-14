class Solution(object):
    def maximumWealth(self, accounts):
        list_1 = []

        for i in accounts:
            list_1.append(sum(i))

        return max(list_1)
        