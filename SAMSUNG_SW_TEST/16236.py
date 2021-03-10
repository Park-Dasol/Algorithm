# 물고기들과의 거리 재는 함수 bfs
def fish(y, x):
    global w, visit
    q = []
    cnt = 0
    q.append((y, x, cnt))
    while q:
        (y, x, cnt) = q.pop(0)
        if visit[y][x] > cnt :
            visit[y][x] = cnt
            for dir in range(4):
                newy = y + dy[dir]
                newx = x + dx[dir]
                #네가지 방향을돌면서 상어무게보다 작거나 같은곳과 이미 방문했다면 그거리가 더 가까운곳일경우 큐에 추가
                if newy >= 0 and newy < N and newx >= 0 and newx < N :
                    if matrix[newy][newx] <= w and visit[newy][newx] > cnt +1:
                        q.append((newy, newx, cnt+1))

# 잡아먹을 물고기를 찾으러
def get_time(y, x):
    global w, res, visit, bob
    minR = 0
    minC = 0
    minT = N**2
    flag = False
    for i in range(N):
        for j in range(N):
            #매트릭스를 돌면서 상어의 무게보다 작고, 가장 단거리인것을 찾는다.
            #가장 위에 가장 왼쪽의 라는 조건은 for문을 돌면서 자동으로 해결
            if matrix[i][j] > 0 and matrix[i][j] < w and visit[i][j] < minT and visit[i][j] >0:
                # flag로 먹을 물고기가 있음을 알려준다
                flag = True
                minT = visit[i][j]
                minR = i
                minC = j
    # 조건에 맞는 물고기가 있다면
    if flag:
        # bob으로 물고기 수를 센다.
        bob += 1
        # res에 시간을 더한다.
        res += minT
        # 원래 아기상어 자리는 0, 잡아먹은 자리로 상어를 이동
        matrix[y][x] = 0
        matrix[minR][minC] = 9
        # 먹은 물고기수가 아기 상어 무게와 같다면 몸무게를 늘이고, bob을 0으로 초기화
        if bob == w:
            w += 1
            bob = 0
        return True
    else:
        return False

#아기상어의 위치를 찾아서 다른 함수를 실행한다.
def shark():
    global w, res, visit, bob
    visit = [[N**2] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 9:
                #상어를 찾으면 물고기들과의 거리를 재는 함수로 이동
                fish(i, j)
                #물고기들과의 거리를 찾았으면 조건에 맞는 물고기를 먹으러 간다.
                # 물고기를 먹었다면 True 그렇지 않다면 False
                if get_time(i, j):
                    return True
                else:
                    return False




N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]


bob = 0
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
res = 0
w = 2
t = True
#더 먹을 물고기가 있는동안 while문을 반복한다.
while t:
    #물고기를 먹었는지 True, False 값으로 확인한다.
    t = shark()

print(res)
