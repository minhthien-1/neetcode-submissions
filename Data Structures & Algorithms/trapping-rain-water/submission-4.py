
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        total_water = 0
        while left <= right:
            if max_left < max_right:
                if max_left > height[left]:
                    total_water += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1

            else:
                if max_right > height[right]:
                    total_water += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1
        return total_water