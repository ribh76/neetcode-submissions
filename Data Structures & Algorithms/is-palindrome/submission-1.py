class Solution:
    def isPalindrome(self, s: str) -> bool:
       cleaned = ''.join(chars.lower() for chars in s if chars.isalnum())
       reverse = cleaned[::-1]
       
       if cleaned == reverse: 
           return True
       else: 
           return False