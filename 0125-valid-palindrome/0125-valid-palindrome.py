class Solution:
    def isPalindrome(self, s: str) -> bool:
    #initiating two pointers one from start and one from the end
        m , n = 0 , len(s) - 1
    
    #using a while loop to ensure that the pointers don't cross each other
        while m < n:
    # if the element in consideration is not alphanumeric as checked by our function, we increment its pointer to check for the next element.
            while m < n and not self.alphanum(s[m]):
                m+=1
            while n > m and not self.alphanum(s[n]):
                n-=1      
    # once we have established that the element in consideration is alphanumeric, we check if it is lower and compare the element in the start and in the end. We return false if they are not same as then it won't be a palindrome. We increment the starting counter and decrease the ending counter to check next if not false.
            if s[m].lower() != s[n].lower():
                return False
            m , n = m+1, n-1
        
        return True
                
        
        
    #defining a function to check if the element in consideration is alphanumeric or not
    def alphanum(self, i):
        return(ord('A') <= ord(i) <= ord('Z') or
        ord('a') <= ord(i) <= ord('z') or
        ord('0') <= ord(i) <= ord('9'))