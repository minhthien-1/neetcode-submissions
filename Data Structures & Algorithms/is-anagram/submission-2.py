class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0]*26
        for i in s:
            a[ord(i)-97] += 1
        for i in t:
            a[ord(i)-97] -= 1
        for counts in a:
            if counts != 0:
                return False
        return True