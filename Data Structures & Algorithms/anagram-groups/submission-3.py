class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count1 = {}
        for i in strs:
            word = "".join(sorted(i))
            if word in count1:
                count1[word].append(i)
            else:
                count1[word] = [i]
        return list(count1.values())

             