class Solution:
    def maxArea(self, height: List[int]) -> int:
        left  = 0
        size = len(height)
        right = size - 1
        max_area = 0
        while left < right:
            min_height = min(height[left], height[right])
            area = min_height * (right - left) 
            max_area = max(area, max_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area            