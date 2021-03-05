import pprint
def makesets(k):
    if k >= len(cams):
        visit_check()
        return
    cam = cams[k]
    if area[cam[0]][cam[1]] == 2:
        for i in range(2):
            sets[k] = i
            makesets(k+1)
            sets[k] = 0
    elif area[cam[0]][cam[1]] == 5:
        sets[k] = 1
        makesets(k + 1)
        sets[k] = 0
    else :
        for i in range(4):
            sets[k] = i
            makesets(k+1)
            sets[k] = 0

def visit_check():
    global minCnt
    for i in range(len(cams)):
        cam = cams[i]
        y = cam[0]
        x = cam[1]
        type = area[y][x]
        dir = sets[i]
        get_color(y, x, type, dir)
    # pprint.pprint(visit)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 0 and visit[i][j] == 0 :
                cnt += 1
            else :
                visit[i][j] = 0
    if cnt < minCnt:
        minCnt = cnt



def get_color(i, j, type, dir):
    flag = True
    y = i
    x = j
    if type == 1:
        while flag:
            newy = y + dy[dir]
            newx = x + dx[dir]
            if newy >= 0 and newy < N and newx >= 0 and newx < M and area[newy][newx] != 6:
                visit[newy][newx] = 1
                y = newy
                x = newx
            else :
                flag = False
                return
    elif type == 2 :
        while flag:
            newy = y + dy[dir]
            newx = x + dx[dir]
            if newy >= 0 and newy < N and newx >= 0 and newx < M and area[newy][newx] != 6:
                visit[newy][newx] = 1
                y = newy
                x = newx
            else :
                if dir >= 0 and dir <2  :
                    dir += 2
                    y = i
                    x = j
                else :
                    flag = False
                    return
    elif type == 3:
        cnt =0
        while flag:
            newy = y + dy[dir]
            newx = x + dx[dir]
            if newy >= 0 and newy < N and newx >= 0 and newx < M and area[newy][newx] != 6:
                visit[newy][newx] = 1
                y = newy
                x = newx
            else:
                if cnt == 0 :
                    cnt += 1
                    dir = (dir + 1) % 4
                    y = i
                    x = j
                else :
                    flag = False
                    return
    elif type == 4 :
        cnt =0
        while flag:
            newy = y + dy[dir]
            newx = x + dx[dir]
            if newy >= 0 and newy < N and newx >= 0 and newx < M and area[newy][newx] != 6:
                visit[newy][newx] = 1
                y = newy
                x = newx
            else:
                if cnt < 2 :
                    cnt += 1
                    dir = (dir + 1) % 4
                    y = i
                    x = j
                else :
                    flag = False
                    return
    else:
        for d in range(4):
            flag = True
            y = i
            x = j
            while flag:
                newy = y + dy[d]
                newx = x + dx[d]
                if newy >= 0 and newy < N and newx >= 0 and newx < M and area[newy][newx] != 6:
                    visit[newy][newx] = 1
                    y = newy
                    x = newx
                else:
                    flag = False
                    break



N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
cams = []
minCnt = M * N
for i in range(N):
    for j in range(M):
        if area[i][j] > 0 and area[i][j] < 6 :
            cams.append([i, j])
sets = [0] * len(cams)
makesets(0)

print(minCnt)


