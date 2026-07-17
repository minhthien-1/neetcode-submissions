class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}

        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        
        danh_sach = sorted(a.items(), key = lambda x: x[1], reverse=True)

        ket_qua = []
        for i in range(k):
            ket_qua.append(danh_sach[i][0])
        
        return ket_qua