class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for i in strs:
            a = [0]*26
            for j in i:
                a[ord(j)-97] += 1
            ck = tuple(a)
            if ck in x: 
                x[ck].append(i)
            else:
                x[ck] = [i]
        return list(x.values())

