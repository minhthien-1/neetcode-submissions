class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        hop1 = [1]*n
        hop2 = [1]*n
        
        tich_luy_trai = 1
        for i in range(n):
            hop1[i] = tich_luy_trai
            tich_luy_trai *= nums[i]

        tich_luy_phai = 1
        for i in range(n-1,-1,-1):
            hop2[i] = tich_luy_phai
            tich_luy_phai *= nums[i]
        
        ketqua = []
        for i in range(n):
            ketqua.append(hop1[i] * hop2[i])
        
        return ketqua