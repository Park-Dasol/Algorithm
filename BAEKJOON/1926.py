from collections import deque


def grim(i, j):
    global maxC
    q = deque()
    q.append((i, j))
    c = 0
    while q:
        y,x = q.popleft()
        matrix[y][x]= 0
        c += 1
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if ny >= 0 and ny < n and nx >= 0 and nx < m and matrix[ny][nx]:
                matrix[ny][nx]= 0
                q.append((ny, nx))

    if c > maxC:
        maxC = c

    # for dir in range(4):
    #     ny = y + dy[dir]
    #     nx = x + dx[dir]
    #     if ny >= 0 and ny < n and nx >= 0 and nx < m and matrix[ny][nx]:
    #         grim(ny, nx, c+ 1)


n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
cnt = 0
maxC = 0
for i in range(n):
    for j in range(m):
        if matrix [i][j]:
            cnt += 1
            grim(i, j)


print(cnt)
print(maxC)



