class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negated_nums = [-num for num in nums]
        heapq.heapify(negated_nums)
        kth_element = None
        for i in range(k):
            kth_element = heapq.heappop(negated_nums)
        return -kth_element