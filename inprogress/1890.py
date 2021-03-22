def jump(y, x):
    global cnt
    if y == N-1 and x == N-1:
        cnt +=1
        return
    if matrix[y][x] != 0 :
        for dir in range(2):

            ny = y + (dy[dir] * matrix[y][x])
            nx = x + (dx[dir] * matrix[y][x])
            if ny >= 0 and ny < N and nx >= 0 and nx < N :
                jump(ny, nx)



N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dy = [1, 0]
dx = [0, 1]
jump(0, 0)



print(cnt)