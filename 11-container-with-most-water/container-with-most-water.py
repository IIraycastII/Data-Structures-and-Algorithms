class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1

        a = 0

        while left != right:
            cal = min(height[left], height[right]) * (right - left)
            if cal > a:
                a = cal

            if min(height[left], height[right]) == height[left]:
                left += 1
            elif min(height[left], height[right]) == height[right]:
                right -= 1
        
        return a