class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = max(nums)
        currMin, currMax = 1, 1

        for i in nums:
            if i == 0:
                currMin, currMax = 1,1
                continue

            currMax, currMin = max(currMin*i, currMax*i, i), min(currMin*i, currMax*i, i)
        
            if currMax > maxProd:
                maxProd = currMax
            
        return maxProd
