class Solution(object):
    def checkIfPangram(self, sentence):
        list_1 = []
        for i in sentence:
            list_1.append(i)
        
        if len(list(set(list_1))) == 26:
            return True
        else:
            return False