class Solution(object):
    def heightChecker(self, heights):
        heights_2 = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != heights_2[i]:
                count += 1
        
        return count