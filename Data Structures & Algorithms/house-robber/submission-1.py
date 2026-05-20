class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        max_array = [0] * len(nums)
        max_array[0] = nums[0]
        max_array[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            max_array[i] = max(nums[i] + max_array[i-2], max_array[i-1])
        return max(max_array)
        