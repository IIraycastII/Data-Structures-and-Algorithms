class Solution(object):
    def topKFrequent(self, nums, k):
        list_1 = []
        for i in Counter(nums).most_common(k):
            list_1.append(i[0])
        
        return list_1