from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        start_r = start_c = -1
        litter_index = {}

        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c

                elif classroom[r][c] == 'L':
                    litter_index[(r, c)] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0


        target_mask = (1 << litter_count) - 1

        queue = deque()
        queue.append((start_r, start_c, energy, 0, 0))


        visited = {
            (start_r, start_c, energy, 0)
        }

        directions = [
            (1, 0),  
            (-1, 0), 
            (0, 1),  
            (0, -1)  
        ]

        while queue:

            r, c, current_energy, mask, moves = queue.popleft()

            if mask == target_mask:
                return moves

            if current_energy == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = current_energy - 1
                new_mask = mask


                if classroom[nr][nc] == 'L':
                    bit = litter_index[(nr, nc)]
                    new_mask |= (1 << bit)


                if classroom[nr][nc] == 'R':
                    new_energy = energy

                state = (nr, nc, new_energy, new_mask)

                if state in visited:
                    continue

                visited.add(state)

                queue.append(
                    (nr, nc, new_energy, new_mask, moves + 1)
                )

        return -1