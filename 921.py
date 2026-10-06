class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        additions = 0

        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    additions += 1

        additions += len(stack)

        return additions