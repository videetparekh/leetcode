class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == "]":
                str_to_repeat = ""
                num = ""
                while stack[-1] != "[":
                    str_to_repeat = stack.pop() + str_to_repeat
                stack.pop() # Remove "["
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(str_to_repeat*int(num))
            else:
                stack.append(char)
        return "".join(stack)

