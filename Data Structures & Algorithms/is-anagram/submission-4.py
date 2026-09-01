class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for a in s:
            if a in count_s:
                count_s[a] += 1
            else:
                count_s[a] = 1
        count_t = {}
        for b in t:
            if b in count_t:
                count_t[b] += 1
            else:
                count_t[b] = 1
        return count_s == count_t
        