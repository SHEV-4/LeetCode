# Two Sum
# 28.10.2025 9:30
# Runtime 21ms, 65.3% 
# Memory 18.88mb, 51.21%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for index, num in enumerate(nums):
            if (target - num) in dict_nums:
                return [dict_nums[target - num],index]
            else:
                dict_nums[num] = index
