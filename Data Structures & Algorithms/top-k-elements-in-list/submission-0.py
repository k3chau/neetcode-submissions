class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newArray = []
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        for i in range(k):
            hashMapkey = max(hashMap, key = hashMap.get)
            newArray.append(hashMapkey)
            hashMap.pop(hashMapkey)
        return newArray
                


        