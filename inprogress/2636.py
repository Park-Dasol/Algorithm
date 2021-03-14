import pprint

def cheese(y, x):
    global t
    t += 1
    visit = [[0]*C for _ in range(R)]
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if ny >= 0 and ny < R and nx >=0 and nx < C and visit[ny][nx] == 0:
            if matrix[ny][nx] == 1:
                matrix[ny][nx] = 2
                visit[ny][nx] = 1
            elif matrix[ny][nx] == 0 :
                visit[ny][nx] = 1
                cheese(ny, nx)
    melt()


def melt():
    global cnt, dnt
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 2:
                cnt += 1
                matrix[i][j] = 0
            elif matrix[i][j] == 1:
                cnt += 1
                dnt += 1
    pprint.pprint(matrix)
    if dnt > 0:
        cheese(0, 0)




R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
t = 0
cnt = 0
dnt = 0

cheese(0, 0)


print(cnt)
print(t)