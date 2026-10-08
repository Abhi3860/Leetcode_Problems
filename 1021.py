class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = ''
        start,end = 0,0
        for c,i in enumerate(s):
            if i == "(":
                stack.append(i)
            else:
                stack.pop()
            if not stack:
                end = c
                res += s[start+1:end]
                start = end+1
        return res