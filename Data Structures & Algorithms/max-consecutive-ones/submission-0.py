class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones_streak = 0 
        max_streak = 0
        for num in nums:
            if num == 1:
                ones_streak += 1
                max_streak = max(max_streak, ones_streak)
            else:
                ones_streak = 0
        return max_streak