class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        hashMap = {}
        for i, nums in enumerate(nums):
            if target - nums not in hashMap:
                hashMap[nums] = i
            else:
                answer.extend([hashMap[target-nums],i])
        return answer
