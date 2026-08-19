class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        from collections import defaultdict
        
        row_blocks = defaultdict(int)
        
        for row, seat in reservedSeats:
            if 2 <= seat <= 5:
                row_blocks[row] |= 1
            if 4 <= seat <= 7:
                row_blocks[row] |= 2
            if 6 <= seat <= 9:
                row_blocks[row] |= 4
                
        total_families = (n - len(row_blocks)) * 2
        
        for blocks in row_blocks.values():
            if blocks == 0:
                total_families += 2
            
            elif (blocks & 1) == 0:
                total_families += 1
            elif (blocks & 4) == 0:
                total_families += 1
            elif (blocks & 2) == 0:
                total_families += 1
                
        return total_families