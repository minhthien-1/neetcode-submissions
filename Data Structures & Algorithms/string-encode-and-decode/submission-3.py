class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            do_dai = str(len(i))
            res = res + do_dai + "#" + i
        return res 
    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            do_dai = int(s[i:j])
            chuoi_goc = s[j + 1 : j + 1 + do_dai]

            ret.append(chuoi_goc)
            i = j + 1 + do_dai
        return ret