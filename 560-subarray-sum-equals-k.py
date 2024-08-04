class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_to_idx = {0: 1}
        prefix_sum = 0
        ct = 0

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in sum_to_idx:
                ct += sum_to_idx[prefix_sum-k]
            sum_to_idx[prefix_sum] = sum_to_idx.get(prefix_sum, 0) + 1
        
        return ct
                
