from collections import defaultdict
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        points1 = []
        points2 = []

        n = len(img1)

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    points1.append((r, c))

                if img2[r][c] == 1:
                    points2.append((r, c))

        shifts = defaultdict(int)

        for r1, c1 in points1:
            for r2, c2 in points2:
                dr = r2 - r1
                dc = c2 - c1

                shifts[(dr, dc)] += 1

        return max(shifts.values(), default=0)