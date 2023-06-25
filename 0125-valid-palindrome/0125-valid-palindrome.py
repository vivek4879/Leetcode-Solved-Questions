class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''
        for i in s:
            if 65<= ord(i) <=90:
                y=0
                y = ord(i) + 32
                x = x + chr(y)
            if 97<= ord(i) <= 122 or 48<= ord(i) <= 57:
                x = x + i
        if x == x[::-1]:
            return True
        
        return False