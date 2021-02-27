import pprint

def get_wall(cnt):
    if cnt == 3:
        # pprint.pprint(matrix)
        virus_check()
        return
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                get_wall(cnt + 1)
                matrix[i][j] = 0



def virus_check():
    global minVirus
    visit = [[0]* M for _ in range(N)]
    q = viruslist[:]
    cnt = 0
    while q :
        (y, x) = q.pop(0)
        visit[y][x] = 1
        cnt += 1
        if cnt >= minVirus:
            break
        for dir in range(4):
            newy = y + dy[dir]
            newx = x + dx[dir]
            if newx>= 0 and newx < M and newy >=0 and newy < N :
                if matrix[newy][newx] == 0 and visit[newy][newx] == 0 :
                    q.append((newy, newx))
    # print(minVirus)
    if cnt < minVirus :
        minVirus = cnt
        print(minVirus)
        pprint.pprint(matrix)
        pprint.pprint(visit)





N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

maxArea = 0
wall = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
viruslist = []
safelist = []

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            wall += 1
        elif matrix[i][j] == 0 :
            safelist.append([i,j])
        elif matrix[i][j] == 2:
            viruslist.append((i, j))
minVirus = N * M - len(viruslist) - wall
get_wall(0)
print(minVirus)
print(N*M - minVirus - wall - 3 + len(viruslist))

