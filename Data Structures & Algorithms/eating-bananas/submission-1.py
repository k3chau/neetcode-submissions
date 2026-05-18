class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ok(piles,k):
            hours = 0
            for pile in piles:
                time = math.ceil(pile / k)
                hours += time
            return hours <= h

        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if(ok(piles,mid)):
                right = mid
            else:
                left = mid + 1
        return left
                

            


