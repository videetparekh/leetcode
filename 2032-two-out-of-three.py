class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ctr = {}
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)

        for num in nums1:
            ctr[num] = ctr.get(num, 1)
        
        for num in nums2:
            ctr[num] = ctr.get(num, 0) + 1

        for num in nums3:
            ctr[num] = ctr.get(num, 0) + 1
        
        return [k for k,v in ctr.items() if v >= 2]
