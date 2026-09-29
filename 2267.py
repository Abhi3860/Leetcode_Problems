class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0] * (m + n) for _ in range(n)] for _ in range(m)]    
        partrack = 0
        if (m + n - 1) % 2 != 0:
            return False
        i,j = 0,0
        def recursMove(i,j, partrack):
            if partrack <0:
                return False
            if dp[i][j][partrack] == -1:
                return False
            
            temp = partrack
            if grid[i][j] == '(':
                partrack +=1
            else:
                partrack -=1

            if partrack<0:
                return False
            if i == m-1 and j == n-1:
                return partrack == 0
            if j+1 < n:
                if recursMove(i,j+1,partrack):
                    return True
            if i+1<m:
                if recursMove(i+1,j,partrack):
                    return True

            dp[i][j][temp] = -1
            return False

        return recursMove(i,j,partrack)

        

        