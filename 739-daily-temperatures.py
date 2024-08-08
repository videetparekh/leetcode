class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # Brute Force 
        # # Time: O(n^2), Space: O(1)
        # answers = [0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             answers[i] = j-i
        #             break
        # return answers
        
        
        # # Monotonically Decreasing Stack
        # Time: O(n), Space: O(n)
        stack = []
        answers = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < temp:
                    prev_temp, j = stack.pop()
                    answers[j] = i-j
            stack.append((temp, i))
        return answers
