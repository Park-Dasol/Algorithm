def tetris():
    # 반복문을 돌면서 각각의 자리에서 5가지의 테트리스를 모두 확인한다
    for i in range(N):
        for j in range(M):
            straight(i, j)
            square(i, j)
            tetromino(i, j)


# 네칸의 값을 더한 값과 maxVal과 비교해서 최대값을 구한다.
def compare(temp):
    global maxVal
    if maxVal < temp :
        maxVal = temp

# 직선
def straight(y, x):
    # j의 값에 따라 수평, 수직
    for j in range(2):
        temp = 0
        # 4칸을 따짐
        for i in range(4):
            newy = y + (dy[j] * i)
            newx = x + (dx[j] * i)
            if newy >= 0 and newy < N and newx >= 0 and newx < M :
                temp += matrix[newy][newx]
            else :
                break
        compare(temp)

# 사각형 : (y,x) 자리에서 두가지 방향값과 그 사이 대각선 값을 더한다.
def square(y, x):
    temp = matrix[y][x]
    for i in range(2):
        newy = y + dy[i]
        newx = x + dx[i]
        if newy >= 0 and newy < N and newx >= 0 and newx < M:
            temp += matrix[newy][newx]
        else:
            return
    newy = y + sy[0]
    newx = x + sx[0]
    if newy >= 0 and newy < N and newx >= 0 and newx < M:
        temp += matrix[newy][newx]
    else:
        return
    compare(temp)

# L, J, T, S, Z 형은 모두 여기서 구한다.
def tetromino(y, x):
    # (y,x) 자리와 한칸씩 떨어진 두가지 방향값은 동일한데 그걸 4방향을 한다.
    for i in range(4):
        temp = matrix[y][x]
        flag = False
        # 첫번째 , 두번째 방향으로 한칸씩 떨어진 칸의 값을 더한다.
        for j in range(2):
            dir = (i + j) % 4
            newy = y + dy[dir]
            newx = x + dx[dir]
            if newy >= 0 and newy < N and newx >= 0 and newx < M:
                temp += matrix[newy][newx]
                if j:
                    # 두가지 방향을 모두 통과했을때만 flag를 True로 해준다.
                    flag = True
            else:
                break
        # 두가지 방향을 모두 했다면 마지막 한칸을 더하러 각각의 함수로 간다.
        if flag:
            getT(y, x, temp, dir)
            getL(y, x, temp, dir)
            getJ(y, x, temp, dir)
            getS(y, x, temp, dir)
            getZ(y, x, temp, dir)

# T는 tetromino 함수에서 가장 마지막 방향보다 한 방향 더 간것을 더한다.
def getT(y, x, temp, dir):
    dir = (dir + 1) % 4
    newy = y + dy[dir]
    newx = x + dx[dir]
    if newy >= 0 and newy < N and newx >= 0 and newx < M:
        compare(temp + matrix[newy][newx])

# L은 tetromino 첫번째 방향에서 2칸 떨어진 값을 더한다.
def getL(y, x, temp, dir):
    dir = (dir + 3) % 4
    newy = y + ly[dir]
    newx = x + lx[dir]
    if newy >= 0 and newy < N and newx >= 0 and newx < M:
        compare(temp + matrix[newy][newx])

# J는 tetromino 두번째 방향에서 2칸 떨어진 값을 더한다.
def getJ(y, x, temp, dir):
    newy = y + ly[dir]
    newx = x + lx[dir]
    if newy >= 0 and newy < N and newx >= 0 and newx < M:
        compare(temp + matrix[newy][newx])

# S는 tetromino 두번째 방향으로 대각선 떨어진 값을 더한다.
def getS(y, x, temp, dir):
    newy = y + sy[dir]
    newx = x + sx[dir]
    if newy >= 0 and newy < N and newx >= 0 and newx < M:
        compare(temp + matrix[newy][newx])

# Z는 tetromino 반시계 방향으로 대각선 떨어진 값을 더한다.
def getZ(y, x, temp, dir):
    dir = (dir + 2) % 4
    newy = y + sy[dir]
    newx = x + sx[dir]
    if newy >= 0 and newy < N and newx >= 0 and newx < M:
        compare(temp + matrix[newy][newx])


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

maxVal = 0

# 상하좌우 1칸씩
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 상하좌우로 2칸씩
sy = [1, 1, -1, -1]
sx = [1, -1, -1, 1]

# 대각선 상하좌우
ly = [0, 2, 0, -2]
lx = [2, 0, -2, 0]

tetris()

print(maxVal)
