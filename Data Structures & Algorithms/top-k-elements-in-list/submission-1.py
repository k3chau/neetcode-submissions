import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = {}
        result = []
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] = 1
        for num, freq in count.items():
            heapq.heappush(heap,(-freq,num))
        for i in range(k):
            freq, negnum = heapq.heappop(heap)
            num = negnum
            result.append(num)
        return result
            
        


        