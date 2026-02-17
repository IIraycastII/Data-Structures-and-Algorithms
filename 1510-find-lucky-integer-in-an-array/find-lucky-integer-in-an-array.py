class Solution(object):
    def findLucky(self, arr):
        list_1 = []
        for i in arr:
            if i == arr.count(i):
                list_1.append(i)
        
        if len(list_1) > 0:
            return max(list_1)
        elif len(list_1) == 0:
            return -1
        