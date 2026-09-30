class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        dep = 0
        res = [0]*(len(seq))
        c=0
        for c,i in enumerate(seq):
            if i == '(':
                res[c] = dep%2
                dep +=1
            else:
                dep-=1
                res[c]=dep%2
        return res