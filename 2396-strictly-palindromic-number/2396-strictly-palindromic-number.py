class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        #we iterate starting from 2 and uptop n-1 to include n-2
        for i in range(2, n-1):
        #we store the value of n in another variable m so that we can work on m  
        #we also initiate a string res
            m = n
            res=''
        #to convert to the respective base we use a while look until the m is no longer divisible by i
            while m >= i:
                res= res + (str(m % i))
                m = m//i
            res = res + str(m)
        #we use string manipulation to check if they are palindrome and return false if they are not
            if res != res[::-1]:
                return False
        return True
            