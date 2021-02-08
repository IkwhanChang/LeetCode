class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        n,m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]
        q = collections.deque()
        
        k = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    q.append((i,j))
                    while q:
                        x,y = q.popleft()
                        if visited[x][y]:
                            continue
                        
                        visited[x][y] = True
                        for x1,y1 in [(0,1), (0,-1), (1,0), (-1,0)]:
                            new_x, new_y = x+x1, y+y1
                            if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == "1" and not visited[new_x][new_y]:
                                q.append((new_x, new_y))
                    k += 1
             
        return k
            