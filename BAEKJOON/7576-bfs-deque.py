from collections import deque

def spread():
    while toms :
        y, x = toms.pop()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if ny >= 0 and ny < N and nx >= 0 and nx < M and box[ny][nx] == 0 :
                box[ny][nx] = 1
                after.append((ny, nx))
    if len(after):
        return True
    else:
        return False

def check():
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return False
    return True

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]


toms = deque()
after = []
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            toms.append((i, j))
t = 0
flag = True
while flag:
    t += 1
    flag = spread()
    toms = after[:]
    after = []


if check():
    print(t-1)
else:
    print(-1)

