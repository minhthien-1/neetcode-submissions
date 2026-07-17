class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        dict_ngoac = {")":"(", "}": "{","]":"["}
        for i in s:
            if i in "({[":
                a.append(i)
            else:
                if len(a) == 0:
                    return False              
                ngoac_mo = a.pop()
                if dict_ngoac[i] != ngoac_mo:
                    return False
        return len(a) == 0