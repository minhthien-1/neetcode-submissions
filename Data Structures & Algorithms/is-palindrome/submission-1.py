class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [char.lower() for char in s if char.isalnum()]
        left = 0
        right = len(a) - 1
        while left < right:
            if a[left] != a[right]:
                return False
            left += 1
            right -= 1
        return True