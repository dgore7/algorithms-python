def dfs(grid, x, y, visited):
    visited[x][y] = True
    if x > 0 and grid[x-1][y] == 'X' and not visited[x-1][y]:
        dfs(grid, x-1, y, visited)
    if y < len(grid[0]) - 1 and grid[x][y+1] == 'X' and not visited[x][y+1]:
        dfs(grid, x, y+1, visited)
    if x < len(grid) - 1 and grid[x+1][y] == 'X' and not visited[x+1][y]:
        dfs(grid, x+1, y, visited)
    if y > 0 and grid[x][y-1] == 'X' and not visited[x][y-1]:
        dfs(grid, x, y-1, visited)





for t in range(int(input())):
    n, m = [int(i) for i in input().strip().split()]
    grid = [string for string in input().strip().split(" ")]
    visited = [[False for i in range(m)] for string in grid]
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X' and not visited[i][j]:
                dfs(grid, i, j, visited)
                count += 1
    print(count)


# OOOOXXO
# OXOXOOX
# XXXXOXO
# OXXXOOO

"""
graph = {
    "A" : [],
    "B" : ["A", "C"],
    "C" : ["A"]
}

"""