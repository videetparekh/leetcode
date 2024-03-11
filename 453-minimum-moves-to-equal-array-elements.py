class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_idx = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[min_idx]:
                min_idx = i

        res = 0
        for i in range(n, 0, -1):
            res += nums[i-1] - nums[min_idx]
        
        return res
