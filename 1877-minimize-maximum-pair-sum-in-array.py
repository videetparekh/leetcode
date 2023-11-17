class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1

        maxval = 0
        while i < j:
            if nums[i]+nums[j] > maxval:
                maxval = nums[i]+nums[j]
            i+=1
            j-=1
        return maxval
