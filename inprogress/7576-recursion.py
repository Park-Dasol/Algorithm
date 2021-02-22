import pprint

def tomato(y, x):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    for dir in range(4):
        newy = y + dy[dir]
        newx = x + dx[dir]
        if newy >= 0 and newy < N and newx >= 0 and newx < M:
            if box[newy][newx] == 0 or (box[newy][newx] > 1 and box[newy][newx] > box[y][x] + 1):
                box[newy][newx] = box[y][x] + 1
                tomato(newy, newx)

def mindays():
    maxday = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
            elif box[i][j] > maxday:
                maxday = box[i][j]
    return maxday -1


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
ripe = []
visit = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            ripe.append((i, j))

while ripe:
    y, x = ripe.pop(0)
    tomato(y, x)


answer = mindays()

print(answer)