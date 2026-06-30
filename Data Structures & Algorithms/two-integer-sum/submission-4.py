class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #hashmap to store the complements keys are the values of nums and values are the indexes
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return[hashMap[complement], i]
            hashMap[nums[i]] = i 
            

        