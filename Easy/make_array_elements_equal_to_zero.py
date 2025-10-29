# Make Array Elements Equal to Zero
# 5235ms 5,42%
# 17.85mb 36.95%
# 28.10.2025 
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        curr = [i for i, val in enumerate(nums) if val == 0]
        
        for index in curr:
            for direct in [1, -1]:
                remaining = sum(nums)
                nums_copy = nums[:]
                i = index
                while remaining: 
                    if i >(len(nums_copy) -1) or i < 0: 
                        break; 
                    elif nums_copy[i] == 0: 
                        i += direct
                    else: 
                        direct = -direct
                        nums_copy[i] -= 1
                        remaining -= 1
                        i += direct
                if remaining == 0:
                    count +=1
        return count

# 29.10.2025
# 54ms 34.48%
# 17.85mb 36.95%
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            left += nums[i]
            right -= nums[i]
            if nums[i] != 0: continue
            if left == right: count += 2
            if abs(left - right) == 1: count += 1
        return count
