class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        max_length = 0
        for i in nums:
            if (i-1) in a:
                continue
            else:
                current_length = 1
                current_nums = i
                while (current_nums+1) in a:
                    current_length += 1
                    current_nums += 1
                max_length = max(max_length,current_length)
        return max_length
        