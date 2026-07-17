class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mang = [0] * len(temperatures)
        hop = []
        for i in range(len(temperatures)):
            while hop and temperatures[i] > temperatures[hop[-1]]:
                ngay_dang_duyet = hop.pop()
                khoang_cach = i - ngay_dang_duyet
                mang[ngay_dang_duyet] = khoang_cach

            hop.append(i)
        return mang