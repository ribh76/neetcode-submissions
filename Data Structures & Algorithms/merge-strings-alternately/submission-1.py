class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k, i, j = 0, 0, 0
        result = []
        while k < len(word1) + len(word2) - 1:
            if i < len(word1): 
                result.append(word1[i])
                i+=1 
            if j < len(word2): 
                result.append(word2[j])
                j+=1 
            k+=1
        return "".join(result)
        




            