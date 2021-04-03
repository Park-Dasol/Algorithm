def danji(y, x):
    global cnt
    matrix[y][x] = 0
    cnt += 1
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if ny >= 0 and ny < N and nx >= 0 and nx < N and matrix[ny][nx] :
            danji(ny, nx)

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


result = []
for i in range(N):
    for j in range(N):
        if matrix[i][j]:
            cnt = 0
            danji(i, j)
            result.append(cnt)

result.sort()

print(len(result))
for i in result:
    print(i)

