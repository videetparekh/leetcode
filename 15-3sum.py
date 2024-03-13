class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        n = len(nums)
        results = set()
        for i in range(n-2):
            j = i+1
            k = n-1
            target = nums[i]*-1
            while j < k:
                sumval = nums[j] + nums[k]
                if sumval == target:
                    results.add((nums[i], nums[j], nums[k]))
                    j+=1
                    k-=1
                elif sumval < target:
                    j+=1
                else:
                    k-=1
            
        return list(results)
