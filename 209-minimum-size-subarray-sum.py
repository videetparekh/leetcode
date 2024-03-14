class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, sm = 0, 0, 0
        n = len(nums)
        minlen = math.inf
        while r < n:
            sm += nums[r]
            while sm >= target:
                if r-l+1 < minlen:
                    minlen = r-l+1
                sm -= nums[l]
                l+=1
            r+=1
        return minlen if minlen != math.inf else 0
            
