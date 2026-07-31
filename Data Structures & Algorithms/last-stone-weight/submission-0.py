import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            x = - (heapq.heappop(stones))
            y = -(heapq.heappop(stones))
            if x == y:
                continue
            newStoneY = max(x,y)
            newStoneX = min(x,y)
            newStones = newStoneY - newStoneX
            heapq.heappush(stones,-newStones)
        if len(stones) == 0:
            return 0
        return -heapq.heappop(stones)