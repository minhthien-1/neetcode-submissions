class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            current_height = heights[i]
            l = i
            while l >= 0 and heights[l] >= current_height:
                l -= 1
            r = i
            while r < n and heights[r] >= current_height:
                r += 1
            width = r - l - 1
            area = width * current_height
            if area > max_area:
                max_area = area
        return max_area