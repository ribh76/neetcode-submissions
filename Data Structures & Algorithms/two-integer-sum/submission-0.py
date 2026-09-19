class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            1. add a hashtable. 
            2. add the contents of nums into the keys pair 
            3. add the difference = target - key into the key's value side 
            4. iterate through the array and see if the difference exists in teh array
            5. return teh indices of the key and difference from the array if they exist in array as a list 
        '''

        for index1 in range(len(nums)): 
            for index2 in range(len(nums)): 
                if (index1 != index2) and (nums[index1] + nums[index2] == target): 
                    return [index1, index2]
        else: 
            return []