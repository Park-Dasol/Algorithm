import pprint

def cheese(y, x):
    q = []
    q.append((y,x))
    while q :
        (y, x) = q.pop(0)
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if ny >= 0 and ny < R and nx >=0 and nx < C and visit[ny][nx] == 0:
                if matrix[ny][nx] == 1:
                    matrix[ny][nx] = 2
                    visit[ny][nx] = 1
                elif matrix[ny][nx] == 0 :
                    visit[ny][nx] = 1
                    q.append((ny, nx))


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
    if dnt > 0:
        return True
    else :
        return False




R, C = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(R)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
t = 0
flag = True
while flag:
    t += 1
    cnt = 0
    dnt = 0
    visit = [[0] * C for _ in range(R)]
    cheese(0, 0)
    flag = melt()
print(t)
print(cnt)
