class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s ={}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in s:
                return [s[y],i]
            s[x] = i