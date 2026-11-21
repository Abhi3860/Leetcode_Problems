from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(s)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        last = [-1] * 26          
        new_parent = parent[:]    
        saved = [-1] * n          
        order = []                

        stack = [(0, False)]
        while stack:
            node, exiting = stack.pop()
            c = ord(s[node]) - 97
            if exiting:
                last[c] = saved[node]
                continue

            saved[node] = last[c]
            if saved[node] != -1:
                new_parent[node] = saved[node]
            order.append(node)
            last[c] = node

            stack.append((node, True))
            for ch in children[node]:
                stack.append((ch, False))

        size = [1] * n
        for x in reversed(order):
            if x != 0:
                size[new_parent[x]] += size[x]
        return size