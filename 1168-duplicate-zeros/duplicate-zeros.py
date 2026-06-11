class Solution(object):
    def duplicateZeros(self, arr):
        point = 0
        len_arr = len(arr)
        count_zero = 0

        while point <= len_arr - 1:
            if len(arr) > len_arr:
                arr.pop()
            elif arr[point] == 0 and count_zero == 0:
                arr.insert(point + 1, 0)
                count_zero += 1
            elif arr[point] == 0 and count_zero > 0:
                point += 1
                count_zero = 0
            
            if count_zero == 0:
                point += 1

        return arr