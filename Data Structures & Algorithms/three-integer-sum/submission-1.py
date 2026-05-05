class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1, -1, 0, 1 ,2]
        #{-5:(0,5),}
        answer = set()
        nums.sort()
        for i,num in enumerate(nums):
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] + num == 0:
                    answer.add((nums[left],nums[right],num))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + num < 0:
                    left += 1
                else:
                    right -= 1
        return list(answer)


