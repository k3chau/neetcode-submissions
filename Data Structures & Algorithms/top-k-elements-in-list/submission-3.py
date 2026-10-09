import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        heap = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for key, value in count.items():
            heapq.heappush(heap,(-value,key))
        for i in range(k):
            popped = heapq.heappop(heap)
            result.append((popped[1]))
        return result


        
        
            



        