class Solution:
    def isPalindrome(self, s: str) -> bool:
        #making an emprty string
        x = ''
        
        #going through every character in the given string and checking if it is alphanumeric
        for i in s:
            if i.isalnum():
                x += i.lower()
                
        #checking if x and reverse of x are equal
        return (x == x[::-1])