class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
            steps: 
            1. get length of input array, call it n 
            2. create a new array of 2x lenght of input array, call it big
            3. create a loop thats the length of nums: 
            4. input the nums value at i in big at i and i + n
            5. return big 
        
        '''
        n = len(nums)

        big = [0] * (2 * n)

        for index in range(len(nums)): 
            big[index] = nums[index]
            repeat = index + n
            big[repeat] = nums[index]

        return big
