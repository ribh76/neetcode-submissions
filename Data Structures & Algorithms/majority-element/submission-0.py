class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        limit = len(nums) // 2

        seen = {}
        
        for i in nums: 
            if seen.get(i) == None: 
                seen[i] = 1
            else: 
                seen[i] = seen[i] + 1

        for key in seen: 
            if seen[key] > limit: 
                return key 