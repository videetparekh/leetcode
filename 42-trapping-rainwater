class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        trapped = 0
        max_on_left = [0]
        max_on_right = [0]

        for i in range(1, n):
            max_on_left.append(max(max_on_left[i-1], height[i-1]))
            max_on_right.append(max(max_on_right[i-1], height[n-i]))
        
        max_on_right.reverse()
        
        for i in range(n):
            trapped+= max(0, min(max_on_left[i], max_on_right[i])-height[i])
        return trapped
