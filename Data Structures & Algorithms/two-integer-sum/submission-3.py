class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}  #nums = [3,4,5,6] 
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [hashMap[target-nums[i]],i]
            hashMap[nums[i]] = i 

            

        