import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        map = {}
        result = []
        for num in nums:
            if num in map:
                map[num] +=1
            else:
                map[num] = 1
        for num,freq in map.items():
            heapq.heappush(heap,(-freq,num))
        for i in range(k):
           freq, num = heapq.heappop(heap)
           result.append(num)
        return result



        