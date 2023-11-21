class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        i, j = nums[0], max(nums[0], nums[1])
        for each in nums[2:]:
            rob = max(j, each+i)
            i = j
            j = rob
            
        return max(i, j)
