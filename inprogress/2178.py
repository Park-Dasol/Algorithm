import sys

def miro(y, x, cnt):
    if visit[y][x] <= cnt:
        return
    else:
        visit[y][x] = cnt
    for dir in range(4):
        newy = y + dy[dir]
        newx = x + dx[dir]
        if newx >= 0 and newx < M and newy >= 0 and newy < N:
            if matrix[newy][newx]:
                miro(newy, newx, cnt+1)



# N, M = map(int, input().split())
N, M = sys.stdin.readline().split()
N = int(N)
M = int(M)
matrix = [list(map(int, input())) for _ in range(N)]
maxnum = N * M
visit = [[maxnum]*M for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
miro(0, 0, 1)

print(visit[N-1][M-1])