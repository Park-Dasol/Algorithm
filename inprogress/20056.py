def move(r, c):
    ball = matrix[r][c]
    dis = ball[1] % N
    newy = ( r + dy[ball[2]] * dis + N ) % N
    newx = ( c + dx[ball[2]] * dis + N ) % N
    next = matrix[newy][newx]
    if next[3]:
        if next[2] % 2 != ball[2] % 2:
            matrix[newy][newx][4] = 1
    matrix[newy][newx][0] += ball[0]
    matrix[newy][newx][1] += ball[1]
    matrix[newy][newx][2] = ball[2]
    matrix[newy][newx][3] += 1

    matrix[r][c] = [0] * 5



N, M, K = map(int, input().split())
# m, s, d, c
matrix = [[[0]*5 for _ in range(N)] for _ in range(N)]
info = {}
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    matrix[r-1][c-1] = [m, s, d, 1, 0]

# print(matrix)
for i in range(N):
    for j in range(N):
        if matrix[i][j][3]:
            move(i, j)

print(matrix)