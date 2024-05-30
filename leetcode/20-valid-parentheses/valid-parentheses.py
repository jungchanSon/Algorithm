class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_arr = ('(', '{', '[')
        close_arr = (')', '}', ']')
        open_close = dict()
        open_close[")"] = "("
        open_close["}"] = "{"
        open_close["]"] = "["
        for i, v in enumerate(s):
            stack.append(v)
            while len(stack) >= 2 and stack[-1] in close_arr and open_close[stack[-1]] == stack[-2]:
                stack.pop()
                stack.pop()
            
        if stack:
            return False
        else:
            return True

        
"""
([{}]{[]})
"""