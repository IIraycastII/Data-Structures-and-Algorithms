class Solution(object):
    def mostWordsFound(self, sentences):
        numbers = []
        for i in sentences:
            list_1 = list(i.split())
            numbers.append(len(list_1))
        
        return max(numbers)
