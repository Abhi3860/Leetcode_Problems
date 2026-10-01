
class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] ==')' or s[0]== ']' or s[0] == '}':
            return False
        stack = []
        for c,i in enumerate(s):
            if i == '(' or i == '[' or i=='{':
                stack.append(i)
            if i == ')':
                if len(stack) == 0:
                    return False
                if stack[-1] != '(':
                    return False
                stack.pop()
            if i == ']':
                if len(stack) == 0:
                    return False
                if stack[-1] != '[':
                    return False
                stack.pop()
            if i == '}':
                if len(stack) == 0:
                    return False
                if stack[-1] != '{':
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False