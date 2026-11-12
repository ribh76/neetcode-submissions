class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums: 
            for i in range(len(nums)): 
                if target == nums[i]: 
                    return i
        else: 
            return -1
