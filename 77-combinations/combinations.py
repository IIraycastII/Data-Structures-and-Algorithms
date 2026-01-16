class Solution(object):
    def combine(self, n, k):
        from itertools import combinations

        list_1 = []

        for i in range(1, n + 1):
            list_1.append(i)

        return list(combinations(list_1, k))
        