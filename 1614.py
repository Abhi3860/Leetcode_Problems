class Solution:
    def maxDepth(self, s: str) -> int:
        partrack = 0
        res = 0

        for i in s:
            if i == "(":
                partrack +=1
                if partrack > res:
                    res = partrack
            elif i == ")":
                partrack -=1
        return res
            