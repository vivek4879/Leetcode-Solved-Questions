class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)
        res = r
        while l <= r:
            rate = (l+r) // 2
            hours = 0
            for i in piles:
                hours = hours + math.ceil(i / rate)
                
            if hours <= h:
                res = min(res,rate)
                r = rate - 1
            else:
                l = rate + 1
        return res
                    
       
            
            