class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # Đảm bảo A luôn là mảng ngắn hơn để tối ưu thời gian tìm kiếm nhị phân
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        
        while True:
            i = (l + r) // 2
            j = half - i - 2

            # Xử lý các biên của mảng bằng âm vô cực và dương vô cực
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Kiểm tra xem vách ngăn đã chia mảng hợp lý chưa
            if Aleft <= Bright and Bleft <= Aright:
                # Nếu tổng số phần tử là lẻ
                if total % 2:
                    return float(min(Aright, Bright))
                # Nếu tổng số phần tử là chẵn
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            
            # Nếu phần tử bên trái của A quá lớn, dịch con trỏ phải sang trái
            elif Aleft > Bright:
                r = i - 1
            # Nếu phần tử bên trái của A quá nhỏ, dịch con trỏ trái sang phải
            else:
                l = i + 1