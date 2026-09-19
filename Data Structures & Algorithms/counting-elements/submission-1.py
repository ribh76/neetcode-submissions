class Solution:
    def countElements(self, arr: List[int]) -> int:
        hs = set(arr)
        count = 0

        for i in arr:
            if i + 1 in hs:
                count += 1
        
        return count