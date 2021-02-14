import sys

def miro(r, c, cnt):
    q = []
    q.append((r, c, cnt))
    while q:
        (y, x, dis) = q.pop(0)
        if visit[y][x] <= dis:
            continue
        else:
            visit[y][x] = dis
            for dir in range(4):
                newy = y + dy[dir]
                newx = x + dx[dir]
                if newy >= 0 and  newy < N and newx >= 0 and newx < M:
                    if matrix[newy][newx]:
                        q.append((newy, newx, dis+1))


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