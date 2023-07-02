class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n-1):
            m = n
            res=[]
            while m >= i:
                res.append(str(m % i))
                m = m//i
            res.append(str(m))
            if ''.join(res) != ''.join(res[::-1]):
                return False
        return True
            