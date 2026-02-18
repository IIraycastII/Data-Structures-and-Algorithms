class Solution(object):
    def sortPeople(self, names, heights):
        list_1 = []

        for i in range(len(names)):
            list_1.append(names[heights.index(max(heights))])
            heights[heights.index(max(heights))] = 0
            
        return list_1
